from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show


def addshowpage(request):
    return render(request, "main_app/addanewshow.html")

def createshow(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        newShow = Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['releasedate'],description=request.POST['description'])
        return redirect(f"/shows/{newShow.id}")

def tvshowdetails(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "main_app/tvshowdetails.html", context)

def allshows(request):
    context = {
        "all_the_shows": Show.objects.all()
    }
    return render(request, "main_app/allshows.html", context)
def editshow(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "main_app/editshow.html", context)

def updateshow(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{id}/edit")
    else:
        updatedShow = Show.objects.get(id=id)
        updatedShow.title = request.POST['title']
        updatedShow.network = request.POST['network']
        updatedShow.release_date = request.POST['releasedate']
        updatedShow.description = request.POST['description']
        updatedShow.save()
        messages.success(request, "Blog successfully updated")
        return redirect(f"shows/{updatedShow.id}")

def destroyshow(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")
# Create your views here.
