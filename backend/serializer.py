from rest_framework import serializers
from .models import Base

#class LeadSerializer(serializers.ModelSerializer):
#   class Meta:
#       model = Lead
#       fields = ['name', 'message']

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['min_in', 'max_in', 'min_out', 'max_out', 'repeat_n']

