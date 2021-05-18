from django.contrib import admin
from django.urls import path
from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('main/', MainView.as_view()),
    path('main/', MainView.as_view()),
    path('main/departure/<str:departure>', DepartureView.as_view()),
    path('main/tour/<int:id>', TourView.as_view()),
    path('main/tour/', TourView.as_view()),
    path('admin/', admin.site.urls),
]
