from django.shortcuts import render, Http404, HttpResponse, redirect
from website.models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from website.form import LoginForm

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
        form = LoginForm
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(to='list')
            else:
                return HttpResponse('<h1>Not A USER!</h1>')
    context['form'] = form
    return render(request, 'register_login.html', context)