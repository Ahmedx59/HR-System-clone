from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch, Department




def branches(request):
    branches = Branch.objects.all()
    return render(request, 'company/branches.html', {'branches':branches})


def branchDetails(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    departments = branch.departmentsBranch.all()
    return render(request, 'company/branchDetails.html', {'branch':branch, 'departments':departments})
