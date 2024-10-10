from django.db.models import fields
from rest_framework import serializers
from .models import LabRequests, LabcloudModel, Attachment, AccountInfo


class AccountInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInfo
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class LabRequestsSerializer(serializers.ModelSerializer):
    files = serializers.ListField(child=serializers.FileField(), write_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = LabRequests
        fields = '__all__'

    def create(self, validated_data):
        files = validated_data.pop('files')
        report = super().create(validated_data)
        Attachment.objects.bulk_create([Attachment(report=report, attach=file) for file in files])

        return report

    def update(self, instance, validated_data):
        method = self.context['request'].method
        if method == 'PUT':
            files = validated_data.pop('files')
            Attachment.objects.filter(report=instance).delete()
            Attachment.objects.bulk_create([Attachment(report=instance, attach=file) for file in files])

        return super().update(instance, validated_data)


class LabRequestsNoFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabRequests
        fields = '__all__'

class LabcloudModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabcloudModel
        fields = '__all__'