from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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