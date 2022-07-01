from django.urls import path
from .views import HomeView, SearchView , DetailView

app_name = "scrapper"
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('search/<str:product_name>/', SearchView.as_view(), name='search'),
    path('Detail/<int:id>/', DetailView.as_view(), name='detail')
]
