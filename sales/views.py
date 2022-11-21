from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale

# Create your views here.
def home_view(request):
    hello = "hello world from the view"
    return render(request, 'sales/home.html', {'hello': hello})

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sales_list' # default is 'object_list'
    
class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'