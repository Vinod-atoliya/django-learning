from django.contrib import admin
from django.urls import path
from core.views import home, about,student_list,student_create,student_update,student_delete,user_login,user_logout,register,set_session,get_session,api_about,student_detail_api,StudentAPIView,StudentDetailAPIView
from core import views


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
    path('register/',register,name='register'),
    path(
    'set-session/',
    set_session,
    name='set_session'
),

path(
    'get-session/',
    get_session,
    name='get_session'
),
    path('api/about/',api_about,name='api_about'),
    # path('api/students/<int:id>/',student_detail_api,name='student_detail_api'),
    path('api/students/',StudentAPIView.as_view(),name='student_api'),
    path(
    'api/students/<int:id>/',
    StudentDetailAPIView.as_view(),
    name='student_detail'
)
]