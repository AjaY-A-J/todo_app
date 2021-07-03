# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms
from django .views.generic import ListView
from django .views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskListview(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'
class TaskDetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'
class TaskUpdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

def task_view(request):
    obj1=Task.objects.all()
    if request.method =='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj = Task(name=name, priority=priority,date='date')
        obj.save()
    return render(request,'task_view.html',{'obj1':obj1})
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url =reverse_lazy('cbvtask')


