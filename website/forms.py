from django import forms
from django.db.models import fields

from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname','lname','email','passwd','age']