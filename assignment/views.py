from django.shortcuts import render, redirect
from assignment.models import Student, Marks

def homepage(request):
    return redirect('/students/')

def students(request):
    if request.method == "POST":
        Student.objects.create(
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname'),
            dob=request.POST.get('dob'),
            parent_name=request.POST.get('pname'),
            address=request.POST.get('add'),
            city=request.POST.get('city'),
            phone=request.POST.get('phone')
        )
        return redirect('/students/')

    else:
        students_data = Student.objects.all()
        return render(request, 'index.html', context={'students_data':students_data})


def marks(request):
    if request.method == "POST":
        # Calculate Percentage
        percent = (int(request.POST.get('english')) + int(request.POST.get('maths')) + int(request.POST.get('science')) + int(request.POST.get('hindi')) + int(request.POST.get('ss')))*100 / 500

        student_record = Student.objects.get(id=request.POST.get('studentid'))
        Marks.objects.create(
            student=student_record,
            english=request.POST.get('english'),
            maths=request.POST.get('maths'),
            science=request.POST.get('science'),
            hindi=request.POST.get('hindi'),
            social_science=request.POST.get('ss'),
            percentage=float(f'{percent:.2f}')
        )
        return redirect('/marks/')
    
    else:
        marks_data = Marks.objects.all()
        return render(request, 'marks.html', context={'marks_data': marks_data})


def reports(request):
    marks_data = Marks.objects.filter(percentage__gte=60)
    return render(request, 'reports.html', context={'marks_data':marks_data})