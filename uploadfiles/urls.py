from django.urls import path
from . import views
from uploadfiles.views import IndexView



urlpatterns = [
    path('', (IndexView.as_view()), name='index'),
]
