from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        print(date_from, date_to, chart_type)
    
        qs = Sale.objects.filter(created__date=date_from)
        obj = Sale.objects.get(id=5)
        print(qs)
        print(obj)

    context = {
        'form':form,
    }
    return render(request, 'sales/home.html', context)

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'



'''def sale_list_view(request):
    qs = Sale.objects.all()
    return render(request, 'sales/main.html', {'object_list':qs})

def sale_detail_view(request, pk):
    obj = Sale.objects.get(pk=pk)
    # or
    # obj=get_objects_or_404(Sale, pk=pk)
    return render(request, 'sales/detail.html', {'object':obj})


    in the urls:
    path('sales/' sale_list_view, name='list'),
    path('sales/<pk>' sale_detail_view, name='detail'),
'''