from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeview(request):
    return render(request, 'app1/home.html', {})

@login_required(login_url='/a2/lv/')
def studentview(request):
    form = StudentForm()
    if request.method == 'POST':
        form =StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/sform.html', {'form': form})

@login_required(login_url='/a2/lv/')
def showview(request):
    obj = Student.objects.all()
    return render(request, 'app1/show.html', {'obj':obj})

def updateview(request, pk):
    obj = Student.objects.get(roll=pk)
    form = StudentForm(instance=obj)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/sform.html', {'form': form})

def deleteview(request, x):
    obj = Student.objects.get(roll = x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv/')
    return render(request, 'app1/success.html', {'obj': obj})
