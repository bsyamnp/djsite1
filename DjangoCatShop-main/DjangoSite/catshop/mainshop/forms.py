from .models import Cats
from django.forms import ModelForm,TextInput,Textarea

class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = ["name","description","breed","age"]

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder" :"Имя кота"
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": " Описание кота"
            }),
            "breed": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Порода"
            }),
            "age": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Возраст"
            })
        }