from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404
from .models import Student
from .serializers import StudentSerializer
#for practice
def home(request):
    context = {
        'name': 'Vinod'
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def student_list(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'students.html', context)

@login_required
def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm()

    return render(request, 'student_form.html', {
        'form': form
    })

@login_required
def student_update(request, id):
    
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm(instance=student)

    return render(request, 'student_form.html', {
        'form': form
    })
    
@login_required
def student_delete(request, id):
    
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {
        'student': student
    })
    
def user_login(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('student_list')

        else:

            return render(request, 'login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'login.html')

def user_logout(request):
    
    logout(request)

    return redirect('login')

def register(request):
    
    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            

            return redirect('login')

    else:

        form = UserCreationForm()

    return render(request, 'register.html', {
        'form': form
    })
    
def set_session(request):
    request.session['username']='Vinod'
    return HttpResponse("Session data Saved.")

def get_session(request):
    username= request.session.get('username')
    return HttpResponse(f"Username:{username}")


def api_about(request):

    data = {
        'name': 'Vinod',
        'role': 'Python Developer',
        'technology': 'Django'
    }

    return JsonResponse(data)



def student_detail_api(request,id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return JsonResponse(
            {'error':'Student not found'},
            status=404
        )
    data = {
        'id':student.id,
        'name':student.name,
        'age':student.age,
        'email':student.email
    }
    return JsonResponse(data)

class StudentAPIView(APIView):
    def get(self,request):
        student = Student.objects.all()
        serializer = StudentSerializer(
            student,many=True
        )
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(
            data = request.data
        )
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
        
class StudentDetailAPIView(APIView):
    
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)

        serializer = StudentSerializer(student)

        return Response(serializer.data)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)

        student.delete()

        return Response(
        {
            "message": "Student deleted successfully."
        },
        status=status.HTTP_200_OK)
        
    def put(self, request, id):
    
        student = get_object_or_404(
            Student,
            id=id
        )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def patch(self, request, id):
    
        student = get_object_or_404(
            Student,
            id=id
        )

        serializer = StudentSerializer(
            student,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )