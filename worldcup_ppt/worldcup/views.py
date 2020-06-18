from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.views.generic import CreateView
from django.http import JsonResponse

from worldcup.world_data import world
import folium
import csv
import json
from django.shortcuts import redirect
import urllib.request
from django.http import HttpResponse

def world_view(request):
    return render(request,"worldcup/world_view.html",{"content":world()})