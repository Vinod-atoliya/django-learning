from django.shortcuts import render, redirect,get_object_or_404
from .models import Student
from .forms import StudentForm
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
def student_delete(request, id):
    
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_confirm_delete.html', {
        'student': student
    })