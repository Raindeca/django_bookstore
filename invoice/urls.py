from django.urls import path, re_path
from . import views


app_name = 'invoice'

urlpatterns = [

    # /invoice/
    path('', views.invoice, name='invoice'),

    # /invoice/1
    path('<int:book_id>/', views.buy, name='buy'),

    # /invoice/pdf_view.
    path('pdf_view/', views.ViewPDF.as_view(), name='pdf_view'),

    # /account/pdf_download/
    path('pdf_download/', views.DownloadPDF.as_view(), name='pdf_download'),
]