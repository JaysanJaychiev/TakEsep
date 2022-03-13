from django import forms
from django.contrib.auth.models import Group


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')
    role = forms.ChoiceField(choices=(
                            ('Родительсий комитет', "Родительский комитет"), 
                            ('Родитель', "Родитель")), label='Роль')


    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        user.groups.add(Group.objects.get(name=f"{self.cleaned_data['role']}"))



