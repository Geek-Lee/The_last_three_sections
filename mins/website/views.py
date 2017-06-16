from django.shortcuts import render, Http404, HttpResponse, redirect
from website.models import Video, Ticket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from website.form import LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def listing(request, cate=None):
    context = {}
    if cate is None:
        vids_list = Video.objects.all()
    if cate == 'editors':
        vids_list = Video.objects.filter(editors_choice=True)
    else:
        vids_list = Video.objects.all()
    page_robot = Paginator(vids_list, 9)
    page_num = request.GET.get('page')
    try:
        vids_list = page_robot.page(page_num)
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)
        #raise Http404('EmptyPage')
    except PageNotAnInteger:
        vids_list = page_robot.page(1)
    context['vids_list'] = vids_list
    return render(request, 'listing.html', context)

def index_login(request):
    context = {}
    if request.method == "GET":
        form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='list')
    context['form'] = form
    return render(request, 'register_login.html', context)

def index_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register_login.html', context)

def detail(request, id):
    context = {}
    vid_info = Video.objects.get(id=id)
    try:
        voter_id = request.user.profile.id
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=id)
        like_counts = Ticket.objects.filter(choice='like', video_id=id).count()
        context['user_ticket'] = user_ticket_for_this_video
        context['like_counts'] = like_counts
    except:
        pass
    context['vid_info'] = vid_info
    return render(request, 'detail.html', context)

def detail_vote(request, id):
    voter_id = request.user.profile.id

    try:
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=id)
        user_ticket_for_this_video.choice = request.POST['vote']
        user_ticket_for_this_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, video_id=id, choice=request.POST['vote'])
        new_ticket.save()

    return redirect(to='detail', id=id)