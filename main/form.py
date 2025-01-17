from django import forms
from .models import Note

# Создаем форму чтобы получить данные с помощью форм и засунуть в бз
class FeedbackModels(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title","content"] #? Для inputов скажем