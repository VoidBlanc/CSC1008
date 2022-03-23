from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
import json

from LIFTMAIN.settings import MAPBOX_PUBLIC_KEY, ONEMAP_DEV_URL, ONEMAP_TOKEN
from ..codes.Routes import roadedge_df,roadnode_df
from ..datastructure.Graph import Graph, dijkstra

# Create your views here.
def landing_page(request):
    return render(request, 'landing.html')


@login_required(login_url='/login')
def index(request):
    args = {'title': "Home"}
    if request.user.is_authenticated:
        print(roadedge_df)
        args['mapbox_key'] = MAPBOX_PUBLIC_KEY
        fname = request.user.first_name
        args['fname'] = fname
        return render(request, 'index.html', args)
    else:
        return render(request, 'index.html', args)

def get_address(request):
    search = request.GET.get('search')
    payload = []
    if search:
        pass
    return JsonResponse({'status': True, 'payload': payload})

