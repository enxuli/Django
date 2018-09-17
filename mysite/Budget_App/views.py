from django.shortcuts import render,get_object_or_404
from .models import Plan
from django.views.generic import CreateView


# Create your views here.
def plan_list(request):
    return render(request,'Budget_App/plan-list.html')

def plan_detail(request,plan_slug):
    #fecth the correct project
    plan = get_object_or_404(Plan, slug = plan_slug)
    if request.method == 'GET':
        category_list = Category.objects.filter(plan=plan)
        return render(request, 'Budget_App/plan-detail.html', {'plan': plan, 'expense_list': project.expenses.all(), 'category_list': category_list})

    elif request.method == 'POST':
        # process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, plan=plan, name=category_name)

            Expense.objects.create(
                plan=plan,
                title=title,
                amount=amount,
                category=category
            ).save()

    elif request.method == 'DELETE':
        id = json.loads(request.body)['id']
        expense = Expense.objects.get(id=id)
        expense.delete()

        return HttpResponse('')

    return HttpResponseRedirect(plan_slug)

class PlanCreateView(CreateView):
    model = Plan
    template_name = 'Budget_App/add-plan.html'
    fields = ('name', 'budget')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            ).save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return slugify(self.request.POST['name'])
