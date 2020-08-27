from django.shortcuts import render, get_object_or_404, redirect
from .models import employee


# Create your views here.

def add(request):

    if request.method=='POST':
        empid=request.POST.get('inputId')
        empname=request.POST.get('inputName')
        empemail=request.POST.get('inputEmail')
        empaddress=request.POST.get('inputAddress')
        empcontact=request.POST.get('inputContact')
        empdesign=request.POST.get('inputDesign')
        empsalary=request.POST.get('inputSal')
        empdoj=request.POST.get('inputdoj')
        empwkexp=request.POST.get('inputExp')
        emppcomp=request.POST.get('inputPcomp')
        empdep=request.POST.get('inputEdep')
        empba=request.POST.get('inputBankaccount')

        b=employee(eid=empid, ename=empname, eemail=empemail, eaddress=empaddress, econtact=empcontact , edesign=empdesign, ecursal=empsalary, edoj=empdoj, ewexp=empwkexp, epcomp=emppcomp, edpt=empdep,eba=empba)
        b.save()
        
    return render(request, 'add_emp.html')
    
    
def show(request):

    obj=employee.objects.all()

    return render(request, 'show_emp.html',{'obj':obj})

