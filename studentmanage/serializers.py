from rest_framework import serializers
from .models import StudentBasicInfo


class StudentBasicInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentBasicInfo
        fields = [
            'id',
            'name',
            'student_id',
            'email',
            'phone'
        ]
