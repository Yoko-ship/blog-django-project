from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import generic
from django.utils import timezone
from .models import Note
from .form import FeedbackModels
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = "main/index.html"
    context_object_name = "latest_notes"

    def get_queryset(self) -> QuerySet[Any]:
        return Note.objects.all().order_by("content")

def detail(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    return render(request,"main/detail.html",{"note":note})

@login_required(login_url="/main/accounts/login")
#? Добавляем значение с помощью формы
#* Не забывай добавить это в url
def feedback_form(request):
    if request.method == "POST":
        form = FeedbackModels(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.pub_date = timezone.now()
            note.save()
            return redirect("/main/")
    else:
        form = FeedbackModels()

    
    return render(request,"main/add.html",{"form":form})


#* Обработка для удаление из бз
def delete_note(request,note_id):
    if request.method == "POST":
        note = get_object_or_404(Note,pk=note_id)
        note.delete()
        return redirect("/main/")
    else:
        return redirect("/main/")
    

def edit_note(request,note_id):
    note = get_object_or_404(Note,pk=note_id)
    if request.method == "POST":
        new_title = request.POST.get("title")
        new_content = request.POST.get("content")
        note.title = new_title
        note.content = new_content
        note.save()
        return redirect("/main/")
    

def authentification(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if name and email and password:
            user = User.objects.create_user(name,email,password)
            user.save()
            print("TEST")
            return redirect("/main/")
    return render(request,"registration/form.html")


@login_required(login_url="/main/accounts/login")
def profile(request):
    return render(request,"main/profile.html")
