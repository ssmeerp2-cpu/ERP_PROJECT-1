from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework import viewsets
from erp_app.models import PainterEntry
from .serializers import PainterEntrySerializer
from erp_app.models import BuffingEntry
from .serializers import BuffingEntrySerializer
from erp_app.models import MaskingEntry
from .serializers import MaskingEntrySerializer
from erp_app.models import PaintStirringEntry
from .serializers import PaintStirringEntrySerializer

@method_decorator(csrf_exempt, name='dispatch')
class PainterEntryViewSet(viewsets.ModelViewSet):
    queryset = PainterEntry.objects.all()
    serializer_class = PainterEntrySerializer
    permission_classes = [AllowAny]

def index(request):
    return render(request, 'testing1.html')

def reporting(request):
    return render(request, 'Reporting.html')

class BuffingEntryViewSet(viewsets.ModelViewSet):
    queryset = BuffingEntry.objects.all().order_by("-date")
    serializer_class = BuffingEntrySerializer

class MaskingEntryViewSet(viewsets.ModelViewSet):
    queryset = MaskingEntry.objects.all().order_by("-date")
    serializer_class = MaskingEntrySerializer

class PaintStirringEntryViewSet(viewsets.ModelViewSet):
    queryset = PaintStirringEntry.objects.all().order_by("-date")
    serializer_class = PaintStirringEntrySerializer