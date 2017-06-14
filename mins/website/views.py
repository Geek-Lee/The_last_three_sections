from django.shortcuts import render, redirect, HttpResponse
from website.models import Video

# Create your views here.
def listing(request):
    context = {}
    vids_list = Video.objects.all()
    context['vids_list'] = vids_list
    return render(request, 'listing.html', context)
