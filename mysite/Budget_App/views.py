from django.shortcuts import render,get_object_or_404
from .models import Plan
from django.views.generic import CreateView


# Create your views here.
def plan_list(request):
    return render(request,'Budget_App/plan-list.html')

def plan_detail(request,plan_slug):
    #fecth the correct project
    plan = get_object_or_404(Plan, slug = plan_slug)
    return render(request,'Budget_App/plan-detail.html',{'plan':plan,'expense_list':plan.expenses.all()})

class PlanCreateView(CreateView):
    model = Plan
    template_name = 'Budget_App/add-plan.html'
    fields = ('name', 'budget')
