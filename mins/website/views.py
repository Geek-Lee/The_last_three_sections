from django.shortcuts import render, Http404
from website.models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
