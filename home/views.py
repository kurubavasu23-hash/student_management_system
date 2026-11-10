from django.shortcuts import render,redirect

def home(request):
    return render(request, 'vasu.html')

def home1(request):
    return render(request, 'task1.html')

def home2(request):
    return render(request, 'task2.html')

def home3(request):
    return render(request, 'task3.html')

def home4(request):
    return render(request, 'task4.html')

def home5(request):
    return render(request, 'task5.html')

def home6(request):
    return render(request, 'task6.html')
def home7(request):
    return render(request, 'task7.html')

def home8(request):
    return render(request, 'task8.html')

def home9(request):
    a=10
    b=20
    c=30
    d=40
    return render(request, 'task9.html',{
         "a":a,
            "b":b,
            "c":c,
            "d":d});
def home10(request):
    name="vasu"
    age=21
    address="anantapur"
    return render(request, 'task10.html',{
         "name": name,
         "age":age,
         "address":address});
def home11(request):
    a=10
    b=20
    c=a+b
    return render(request, 'task11.html',{
        "c":c
    });


def home12(request):
    a=10
    b=20
    c=a+b,
    d=a-b,
    e=a*b,
    f=a/b,
    g=a%b
    return render(request, 'task12.html',{
         "c":c,
         "d":d,
         "e":e,
         "f":f,
         "g":g
     });

def home13(request):
    color="red",
    movie="orange",
    brand="King",
    year=2026,
    exp=2027,
    date=2026-10-10

    return render(request, 'task13.html',{
        "color": color,
        "movie":movie,
        "brand":brand,
        "year":year,
        "exp":exp,
        "date":date

    });

def home14(request):
    name=""
    phonenumber=""
    email=""
    if request.method=="POST":
        name=(request.POST["name"])
        phonenumber=(request.POST["phonenumber"])
        email=(request.POST["email"])
    return render(request, 'task14.html',{
        "name":name,
        "phonenumber":phonenumber,
        "email":email,
    })

def home15(request):
    firstname=""
    lastname=""
    email=""
    salary=""
    phonenumber=""
    address=""
    if request.method=="POST":
        firstname=(request.POST["firstname"])
        lastname=(request.POST["lastname"])
        email=(request.POST["email"])
        salary=(request.POST["salary"])
        phonenumber=(request.POST["phonenumber"])
        address=(request.POST["address"])
    return render(request, 'task15.html',{
        "firstname":firstname,
        "lastname":lastname,
        "email":email,
        "salary":salary,
        "phonenumber":phonenumber,
        "address":address,
      })

def home16(request):
    return render(request, 'task16.html')
def home17(request):
    return render(request, 'task17.html')
def home18(request):
    return render(request, 'task18.html')

from .models import student
def vasu19(request):
    if request.method=='POST':
        firstname=request.POST["first_name"]
        lastname=request.POST["lastname"]
        middlename=request.POST["middlename"]
        age=request.POST["age"]
        address=request.POST["address"]

        student.objects.create(firstname=firstname,
                              lastname=lastname,
                              middlename=middlename,
                              age=age,
                              address=address)
        

        return render(request,"successfull.html")
    return render(request,"task19.html")

def successfully(request):
    return render(request,'successfull.html')
from .models import student1
def vasu20(request):
    if request.method=="POST":
        student_name=request.POST.get('student_name')
        email=request.POST.get('email')
        age=int(request.POST.get('age'))
        gender=request.POST.get('gender')
        course=request.POST.getlist('course')
        student1.objects.create(student_name=student_name,
                               email=email,
                               age=int(age),
                               gender=gender,
                               course=",".join(course))
        return render(request,"successfull.html")
    return render(request,"task20.html")
    
        
    