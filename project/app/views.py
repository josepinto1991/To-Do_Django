from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm, RegisterForm

def task_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()
        return render(request, 'html/task_list.html', {'tasks': tasks})
    else:
        return redirect('login')
    
def create_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TaskForm()
        return render(request, 'html/create_task.html', {'form': form})
    else:
        return redirect('login')
def complete_task(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save()
        return redirect('task_list')
    else:
        return redirect('login')

def reopen_task(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id)
        task.completed = False
        task.save()
        return redirect('task_list')
    else:
        return redirect('login')

def delete_task(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('task_list')
    else:
        return redirect('login')

def modify_task(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id)
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')
        else:
            form = TaskForm(instance=task)
        return render(request, 'html/modify_task.html', {'form': form})
    else:   
        return redirect('login')


def index(request):
    return render(request, 'html/index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'html/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  


# from django.http import JsonResponse
# from django.shortcuts import redirect
# from .models import Task

# def delete_task(request, task_id):
#     task = Task.objects.get(id=task_id)
#     task.delete()
#     return JsonResponse({'message': 'Tarea eliminada correctamente'})


# html

# {% extends 'html/base.html' %}

# {% block content %}
#     <div class="container">
        
#         <div class="container-sidebar">
#             <div class="sidebar">
#                 <h3>
#                 <a href="{% url 'create_task' %}">Crear nueva tarea</a> | 
#                 <a href="{% url 'logout' %}">logout 💀</a>
#                 </h3>
#             </div>
#         </div>

#         <h1>Lista de Tareas 📑</h1>
       
#         <ul>
#             {% for task in tasks %}
#                 <li data-task-id="{{ task.pk }}">
#                     <h4>Tarea {{ forloop.counter }}</h4>
                    
#                     {% if task.completed %}
#                         <span class="completed"><p>{{ task.task|linebreaks }}</p></span>
#                         <span class="completed2">Estatus: Completado ✅</span>
#                     {% else %}
#                         <span class="completed2">{{ task.task|linebreaks }}</span> 
#                         <span class="completed2">Estatus: Pendiente ⏳</span>
#                     {% endif %} 
                    
#                     <div class="actions">
#                     {% if task.completed %}
#                         <a href="{% url 'reopen_task' task.pk %}">Reabrir</a> |
#                     {% endif %}
#                     {% if not task.completed %}
#                         <a href="{% url 'complete_task' task.pk %}">Completar</a> |
#                     {% endif %}
#                         <a href="{% url 'modify_task' task.pk %}">Modificar</a>
#                     |   <button onclick="eliminarTarea({{ task.pk }})">Eliminar</button>
#                     </div>
#                 </li>
#             {% endfor %}
#         </ul>
#     </div>

#     <script>
#         function eliminarTarea(taskId) {
#             fetch('{% url 'delete_task' 0 %}'.replace('0', taskId), {
#                 method: 'DELETE',
#                 headers: {
#                     'X-CSRFToken': '{{ csrf_token }}'
#                 }
#             })
#             .then(response => response.json())
#             .then(data => {
#                 document.querySelector(`li[data-task-id="${taskId}"]`).remove();
#             })
#             .catch(error => console.error('Error:', error));
#         }
#     </script>
# {% endblock %}
