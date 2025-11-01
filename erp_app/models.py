from django.db import models

class PainterEntry(models.Model):
    painter_name = models.CharField(max_length=100)
    date = models.DateField()
    part_no = models.CharField(max_length=100)
    grn_no = models.CharField(max_length=100)
    lot_qty = models.IntegerField(null=True, blank=True)
    total_ok = models.IntegerField(null=True, blank=True)
    moulding_chemical = models.IntegerField(null=True, blank=True)
    rep_dust = models.IntegerField(null=True, blank=True)
    rep_scratch = models.IntegerField(null=True, blank=True)
    rep_less_paint = models.IntegerField(null=True, blank=True)
    rep_colour_fin = models.IntegerField(null=True, blank=True)
    rep_light_pass = models.IntegerField(null=True, blank=True)
    rep_ok_qty = models.IntegerField(null=True, blank=True)
    rework_person = models.CharField(max_length=100, null=True, blank=True)
    painter_sign = models.CharField(max_length=100, null=True, blank=True)
    rej_dust = models.IntegerField(null=True, blank=True)
    rej_scratch = models.IntegerField(null=True, blank=True)
    rej_dent = models.IntegerField(null=True, blank=True)
    rej_less_paint = models.IntegerField(null=True, blank=True)
    rej_cut_mark = models.IntegerField(null=True, blank=True)
    rej_paint_flow = models.IntegerField(null=True, blank=True)
    qc_sign = models.CharField(max_length=100, null=True, blank=True)
    judgement = models.CharField(max_length=10, null=True, blank=True)
    line_leader = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.painter_name} - {self.date}"

class BuffingEntry(models.Model):
    date = models.DateField()
    part_code = models.CharField(max_length=50)
    part_description = models.CharField(max_length=200, blank=True, null=True)
    lot_qty = models.IntegerField()
    ok_qty = models.IntegerField()
    ng_qty = models.IntegerField()
    reason_for_ng = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=100)
    incharge = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.part_code} ({self.operator})"

class MaskingEntry(models.Model):
    department = models.CharField(max_length=100)
    date = models.DateField()
    item_description = models.CharField(max_length=200)
    lot_qty = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    ok_qty_after_masking = models.IntegerField()
    reject_qty = models.IntegerField()
    defect = models.TextField(blank=True, null=True)
    judgement = models.CharField(max_length=10)
    prepared_by = models.CharField(max_length=100)
    verify_by = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.item_description} ({self.prepared_by})"

class PaintStirringEntry(models.Model):
    date = models.DateField()
    paint_name = models.CharField(max_length=100)
    paint_code = models.CharField(max_length=100) 
    batch_code = models.CharField(max_length=100)
    pkg_size = models.CharField(max_length=50)
    pkg_references= models.CharField(max_length=100)
    expry_date = models.DateField()
    air_pressure = models.FloatField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    done_by = models.CharField(max_length=100)
    judgement = models.CharField(max_length=10)
    verify_by = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.paint_name} ({self.batch_code})"