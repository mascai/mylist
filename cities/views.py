from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City
from django.db.models import Q
from django.shortcuts import render, get_object_or_404


class HomePageView(ListView):
    model = City
    template_name = 'cities/home.html'
    paginate_by = 3
    page_kwarg = 'city'

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'cities/city_detail.html', {'city': city})


class SearchResultsView(ListView):
    model = City
    template_name = 'cities/search_results.html'
    paginate_by = 3
    page_kwarg = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list