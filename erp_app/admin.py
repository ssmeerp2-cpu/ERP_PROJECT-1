from django.contrib import admin
from erp_app.models import PainterEntry
from erp_app.models import BuffingEntry
from erp_app.models import MaskingEntry
from erp_app.models import PaintStirringEntry

@admin.register(PainterEntry)
class PainterEntryAdmin(admin.ModelAdmin):
    list_display = ('painter_name', 'date', 'part_no', 'grn_no')  # Add other fields as necessary
    search_fields = ('painter_name', 'part_no', 'grn_no')  # Add other fields as necessary

@admin.register(BuffingEntry)
class BuffingEntryAdmin(admin.ModelAdmin):
    list_display = (
        "date", "part_code", "part_description",
        "lot_qty", "ok_qty", "ng_qty", "operator", "incharge"
    )
    search_fields = ("part_code", "part_description", "operator")
    list_filter = ("date", "incharge")

@admin.register(MaskingEntry)
class MaskingEntryAdmin(admin.ModelAdmin):
    list_display = (
        "department","date","item_description","lot_qty","start_time","end_time",
        "ok_qty_after_masking","reject_qty","defect","judgement","prepared_by","verify_by"
    )
    search_fields = ("item_description", "prepared_by")

@admin.register(PaintStirringEntry)
class PaintStirringEntryAdmin(admin.ModelAdmin):
    list_display = (
        "date","paint_name","paint_code","batch_code","pkg_size","pkg_references",
        "expry_date","air_pressure","start_time","end_time","done_by","judgement","verify_by","remarks"
    )
    search_fields = ("paint_name", "paint_code", "batch_code", "done_by")
    list_filter = ("date",)