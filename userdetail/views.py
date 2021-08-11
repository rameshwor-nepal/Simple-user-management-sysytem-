from userdetail.models import Userprofile
from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    userprofile = Userprofile.objects.all()
    return render(request , 'home.html', context={'userdata' :userprofile} )


def adduser(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        Userprofile.objects.create(firstname=firstname, lastname = lastname, mobile = mobile, email = email, address = address)
        return redirect('index')
    return render(request, 'add.html')


def update(request, id):
    userprofile = Userprofile.objects.get(id=id)

    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        
        if (request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('address')):
            Userprofile.objects.filter(id = id).update(firstname=firstname, lastname = lastname, mobile = mobile, email = email, address = address)
            context={'userprofile':userprofile}
        return redirect('index')

    return render(request, 'update.html', context={'userprofile':userprofile})



def detail(request,id):
    userprofile = Userprofile.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('mobile') and request.POST.get('email') and request.POST.get('address'):
                Userprofile.objects.filter(id = id).update(firstname = request.POST.get('firstname'), lastname= request.POST.get('lastname'), mobile = request.POST.get('mobile'), email = request.POST.get('email'), address = request.POST.get('address'))
                context={'userprofile': userprofile}
        return redirect('index')
    return render(request, 'detail.html', context={'userprofile': userprofile})

def delete(request, id):
    usertodelete = Userprofile.objects.get(pk=id)
    usertodelete.delete()
    return redirect('index')