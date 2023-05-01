from django.shortcuts import render, redirect
from .models import Cats
from .forms import CatsForm
from django.views.generic import DetailView,UpdateView,DeleteView
# Create your views here.



def main_page(request):
    cats = Cats.objects.all()
    return render(request,"mainshop/homepage.html",{"cats":cats})

class CatsDetail(DetailView):
    model = Cats
    template_name = "mainshop/detail-cats.html"
    context_object_name = "cats"

class CatsUpdate(UpdateView):
    model = Cats
    template_name = "mainshop/create.html"
    form_class = CatsForm

class CatsDelete(DeleteView):
    model = Cats
    template_name = "mainshop/delete.html"
    success_url = "/"


def create(request):
    error = ""
    if request.method =="POST":
        form = CatsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была неверной"
    form = CatsForm()
    data = {
        "form":form,
        "error":error
    }
    return render(request,"mainshop/create.html",data)