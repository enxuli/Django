from django.shortcuts import render

# Create your views here.
def project_list(request):
    return render(request,'Budget_App/project-list.html')

def project_detail(request,project_slug):
    #fecth the correct project
    return render(request,'Budget_App/project-detail.html')
