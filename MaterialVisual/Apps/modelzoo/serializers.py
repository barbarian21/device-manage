from rest_framework import serializers

from .models import ReportModel,Attachment,ReleaseModel

class ReleaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseModel
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = '__all__'

# class UaxTModelSerializer(serializers.ModelSerializer):

#     attachments = serializers.ListField(
#         child=serializers.ImageField(),
#     )

#     def create(self, validated_data):
#         attachments = validated_data.pop('attachments')
#         uaxt = super().create(validated_data)
#         Attachment.objects.bulk_create(
#             [Attachment(uaxt=uaxt, image=image) for image in attachments]
#         )
#         return uaxt

#     def to_representation(self, instance):
#         self.fields['attachments'] = AttachmentSerializer(many=True)
#         return super().to_representation(instance)


#     class Meta:
#         model = UaxTModel
#         fields = '__all__'
class ReportModelSerializer(serializers.ModelSerializer):
    files = serializers.ListField(child=serializers.FileField(), write_only=True)  # noqa: E501
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = ReportModel
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

        return super().update(instance,validated_data)

class ReportModelNoFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportModel
        fields = '__all__'