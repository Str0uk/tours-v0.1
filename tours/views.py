from django.views.generic.base import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'

class DepartureView(TemplateView):
    template_name = 'departure/departure.html'


class TourView(TemplateView):
    template_name = 'tour/tour.html'
