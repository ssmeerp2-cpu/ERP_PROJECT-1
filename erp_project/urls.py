from django.urls import path, include
from rest_framework.routers import DefaultRouter
from erp_app.api.views import PainterEntryViewSet

router = DefaultRouter()
router.register(r'entries', PainterEntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('erp_app.urls')),
]