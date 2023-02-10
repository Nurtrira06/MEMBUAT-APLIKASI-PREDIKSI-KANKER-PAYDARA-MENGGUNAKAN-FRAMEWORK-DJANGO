from django.urls import path, include
from .views import KankerToPdf

urlpatterns = [

    #pdf
    path('print_pdf', KankerToPdf.as_view(),name='kanker_to_pdf')
   
]