from rest_framework import serializers
from erp_app.models import PainterEntry
from erp_app.models import BuffingEntry
from erp_app.models import MaskingEntry
from erp_app.models import PaintStirringEntry

class PainterEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PainterEntry
        fields = '__all__'

class BuffingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuffingEntry
        fields = '__all__'

class MaskingEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaskingEntry
        fields = '__all__'

class PaintStirringEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintStirringEntry
        fields = '__all__'