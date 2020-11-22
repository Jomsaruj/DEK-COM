from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):

    is_java = forms.BooleanField(label="Java", required=False)
    is_python = forms.BooleanField(label="Python", required=False)
    is_JavaScript = forms.BooleanField(label="JavaScript", required=False)
    is_Csharp = forms.BooleanField(label="C#", required=False)
    is_C = forms.BooleanField(label="C", required=False)
    is_Cpp = forms.BooleanField(label="C++", required=False)
    is_Go = forms.BooleanField(label="Go", required=False)
    is_R = forms.BooleanField(label="R", required=False)
    is_Swift = forms.BooleanField(label="Swift", required=False)
    is_PHP = forms.BooleanField(label="PHP", required=False)
    is_Kotlin = forms.BooleanField(label="Kotlin", required=False)
    is_Ruby = forms.BooleanField(label="Ruby", required=False)
    is_Dart = forms.BooleanField(label="Dart", required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'is_java', 'is_python',
                  'is_JavaScript', 'is_Csharp', 'is_C', 'is_Cpp', 'is_Go', 'is_R', 'is_Swift', 'is_PHP', 'is_Kotlin',
                  'is_Ruby', 'is_Dart')


