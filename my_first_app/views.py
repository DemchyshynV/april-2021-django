from django.shortcuts import render

# Create your views here.
users = ['Max', 'Kira', 'Karina', 'Misha']


def home(request):
    return render(request, 'home.html', {'course': 'april-2021'})


def user(request):
    return render(request, 'users.html', {'users': users})


def test(request, age, name):
    users.append(name)
    return render(request,'test.html', {'age': age, 'name':name})
