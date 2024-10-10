from rest_framework import serializers

from .models import QuestionModel,Attachment,SupportModel

class SupportModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportModel
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
class QuestionModelSerializer(serializers.ModelSerializer):
    files = serializers.ListField(child=serializers.FileField(), write_only=True)  # noqa: E501
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionModel
        fields = '__all__'

    def create(self, validated_data):
        files = validated_data.pop('files')
        question = super().create(validated_data)
        Attachment.objects.bulk_create([Attachment(question=question, attach=file) for file in files])

        return question

    def update(self, instance, validated_data):
        method = self.context['request'].method
        if method == 'PUT':
            files = validated_data.pop('files')
            Attachment.objects.filter(question=instance).delete()
            Attachment.objects.bulk_create([Attachment(question=instance, attach=file) for file in files])

        return super().update(instance,validated_data)

class QuestionModelNoFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionModel
        fields = '__all__'