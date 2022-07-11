from rest_framework import serializers
from holers.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["username"]