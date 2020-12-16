from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
print(dir(auth_views))

urlpatterns = [
    path(r'login/$', auth_views.LoginView, name = 'login'),
    path(r'logout', auth_views.LogoutView, {'next_page': '/successfully_logged_out/'}, name = 'logout'),
    path('index/', views.index),
    path('quiz-list', views.quiz_list, name= 'quizlist'),
    path('quiz-form', views.quiz_form, name = 'quizform'),
    path('quiz-new', views.quiz_new, name='quiznew'),
    path('score', views.form_resp, name = 'form_resp'),
    path('quiz-page', views.qpage, name= 'quiz_page'),

]
