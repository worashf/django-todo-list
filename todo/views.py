from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from  django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib import  messages
from django.urls import reverse_lazy
from  .models import Task


class CreateTask(CreateView):
    model  = Task
    fields = ['title','description','completed']
    success_url  =reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The task was created successfully.")
        return super(CreateTask,self).form_valid(form)

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdate,self).form_valid(form)
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)


class TaskList(ListView):
    model = Task
    context_object_name  ='tasks'

class TaskDetail(DetailView):
    model  = Task
    context_object_name ='task'


def home(request):
    return render(request, 'home.html')


