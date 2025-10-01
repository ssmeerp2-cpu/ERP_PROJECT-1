from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.reporting, name='home'),  # root URL par reporting view
    path('testing1.html/', views.testing1_view, name='testing1'),
    path('api/entries/', views.api_entries_view, name='api_entries'),
    path('reporting/', views.reporting, name='reporting'),
    path('buffing_production.html/', views.buffing_page, name='buffing_page'),
    path('api/buffing-entries/', views.api_buffing_entries_view, name='api_buffing_entries'),
    path('masking_sheet.html/', views.masking_page, name='masking_page'),
    path('api/masking-entries/', views.api_masking_entries_view, name='api_masking_entries'),
    path('paint_stirring.html/', views.paint_stirring_page, name='paint_stirring_page'),
    path('api/paint-stirring-entries/', views.api_dispatch_entries_view, name='api_paint_stirring_entries'),
]