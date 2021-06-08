from django.contrib import admin
from django.urls import path
from tours.views import MainView, DepartureView, TourView

urlpatterns = [
    path('main/', MainView.as_view()),
    path('/', MainView.as_view()),
    path('/departure/', DepartureView.as_view()),  #'main/departure/<str:departure>'
    path('/tour/<int:id>', TourView.as_view()),
    path('/tour/', TourView.as_view()),
    path('admin/', admin.site.urls),
]
