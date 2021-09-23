from django.shortcuts import render, redirect

# Create your views here.
from .models import Member

from .forms import MemberForm

from django.contrib import messages

def home(request):

    all_member = Member.objects.all #bazadagi barcha malumotni olish uchun

    return render(request,'home.html',{'all':all_member})



def join(request):  # sourcery skip: remove-pass-body
    if request.method=='POST':
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            messages.error(request,('Xatolik sodir boldi!! '))
            return redirect('join')
        messages.success(request,'Zur, bazaga qushildi')
        return redirect('home')
    else:
        return render(request,'join.html',{})   