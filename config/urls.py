from django.contrib import admin
from django.urls import path
from core.views import home, about,student_list,student_create,student_update,student_delete,user_login,user_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('about/', about,name='about'),
    path('students/', student_list, name='student_list'),
    path('students/create/', student_create,name='student_create'),
    path('students/<int:id>/edit/',student_update,name='student_update'),
    path('students/<int:id>/delete/',student_delete,name='student_delete'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
]