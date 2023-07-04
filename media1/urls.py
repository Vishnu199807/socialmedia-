from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_post, name='create_post'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
]