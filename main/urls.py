from django.urls import path,include
from . import views

app_name = "main"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("add/",views.feedback_form,name="add_note"),
    path("<int:note_id>",views.detail,name="detail"),
    path("delete/<int:note_id>/",views.delete_note,name="delete"),
    path("edit/<int:note_id>/",views.edit_note,name="edit"),
    path("accounts/register/",views.authentification,name="register"),
    path("accounts/",include('django.contrib.auth.urls')), #* Обработка для Login
    path("accounts/password_reset/",include(('django.contrib.auth.urls'))),
    path("accounts/profile/",views.profile,name="profile"),
]