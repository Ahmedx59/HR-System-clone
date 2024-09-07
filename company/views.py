from django.shortcuts import render, redirect
from .models import Branch, Department




def branches(request):
    branches = Branch.objects.all()
    return render(request, 'company/branches.html', {'branches':branches})


def branch_details(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    departments = branch.departmentsBranch.filter(branch=branch)
    return render(request, 'company/branch_details.html', {'branch':branch, 'departments':departments})


def branch_create(request):
    if request.method == 'POST':
        name = request.POST['branch-name']
        address = request.POST['branch-address']
        phone = request.POST['branch-phone']
        email = request.POST['branch-email']
        Branch.objects.create(
            name= name,
            address= address,
            phone= phone,
            email=email
        )
        return redirect('/company/')

    return render(request,'company/create_branch.html')
