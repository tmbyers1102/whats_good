from django.shortcuts import render
from .models import Checkin, Tag, Author


def home(request):
    context = {
        'checkins': Checkin.objects.all(),
    }
    return render(request, "checkins/home.html", context)

def checkin_detail(request, pk):
    return render(request, "checkins/checkin_detail.html")