from rest_framework import fields, serializers
from fullthrottle_app.models import ActivityPeriod
from django.contrib.auth import get_user_model
User = get_user_model()

# Created a Class to Serializer User Model 
class UserListAPISerializer(serializers.ModelSerializer):
    real_name = serializers.CharField(source='first_name')
    class Meta:
        model = User
        fields = (
            'id','real_name','tz',
        )
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['acitvity_periods'] = ActivityPeriod.objects.filter(user=instance).values('start_time','end_time')
        return representation



