from django.db.models import Count
from django.views.generic import ListView, DetailView
from .models import Citizen, City


class HomePage(ListView):

    template_name = 'mainapp/homepage.html'
    model = Citizen
    extra_context = {}

    def get_context_data(self, **kwargs):
        self.extra_context.update({
            'biggest_cities': City.objects.annotate(
                citizens_count=Count('citizen')
            ).order_by('-citizens_count')[:5]
        })
        return super().get_context_data(**kwargs)

class CityDetail(DetailView):

    model = City
