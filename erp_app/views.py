from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from erp_app.models import PainterEntry
from .api.serializers import PainterEntrySerializer
from erp_app.models import BuffingEntry
from .api.serializers import BuffingEntrySerializer
from erp_app.models import MaskingEntry
from .api.serializers import MaskingEntrySerializer
from erp_app.models import PaintStirringEntry
from .api.serializers import PaintStirringEntrySerializer

def reporting(request):
    return render(request, 'Reporting.html')


def testing1_view(request):
    if request.method == 'GET':
        return render(request, 'testing1.html')

@api_view(["GET", "POST", "PUT"])  # Add this decorator

def api_entries_view(request, pk=None):  # Add pk parameter for updates
    if request.method == "GET":
        if pk:  # If ID is provided, return a single entry
            entry = get_object_or_404(PainterEntry, pk=pk)
            serializer = PainterEntrySerializer(entry)
            return Response(serializer.data)
        entries = PainterEntry.objects.all().order_by("-date")  # Add ordering like other views
        serializer = PainterEntrySerializer(entries, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PainterEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PUT":  # Add this for updates
        entry = get_object_or_404(PainterEntry, pk=pk)
        serializer = PainterEntrySerializer(entry, data=request.data, partial=True)  # partial=True allows partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def buffing_page(request):
    return render(request, "buffing_production.html")
@api_view(["GET", "POST"])
def api_buffing_entries_view(request):
    if request.method == "GET":
        entries = BuffingEntry.objects.all().order_by("-date")
        serializer = BuffingEntrySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BuffingEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def masking_page(request):
    return render(request, "masking_sheet.html")
@api_view(["GET", "POST"])
def api_masking_entries_view(request):
    if request.method == "GET":
        entries = MaskingEntry.objects.all().order_by("-date")
        serializer = MaskingEntrySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MaskingEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def paint_stirring_page(request):
    return render(request, "paint_stirring.html")
@api_view(["GET", "POST"])
def api_dispatch_entries_view(request):
    if request.method == "GET":
        entries = PaintStirringEntry.objects.all().order_by("-date")
        serializer = PaintStirringEntrySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PaintStirringEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)