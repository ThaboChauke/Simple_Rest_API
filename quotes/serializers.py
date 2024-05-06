from rest_framework import serializers
from .models import Quotes

class QuotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id','said_by','quote','anime']
