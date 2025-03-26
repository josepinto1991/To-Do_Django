from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('task_list/', views.task_list, name='task_list'),
    path('create_task/', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('modify_task/<int:task_id>/', views.modify_task, name='modify_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('reopen_task/<int:task_id>/', views.reopen_task, name='reopen_task'),
]    