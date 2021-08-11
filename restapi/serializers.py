from rest_framework import serializers

from .models import MailConf

class MailConfSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return MailConf.objects.create()

    def update(self, instance, validated_data):
        instance.save()
        return instance

    class Meta:
        model = MailConf 
        fields = (
            'id',
            'login',
            'allowed_hosts'
        )
