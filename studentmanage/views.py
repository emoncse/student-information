from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import StudentBasicInfoSerializer
from .models import StudentBasicInfo


class StudentsBasicInfoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = StudentBasicInfoSerializer

    def get_queryset(self):
        queryset = StudentBasicInfo.objects.filter().order_by('-id')
        return queryset

    def retrieve(self, request, pk=None, **kwargs):
        print(kwargs.get('id'))
        queryset = StudentBasicInfo.objects.filter()
        try:
            student_info = get_object_or_404(
                queryset, id=kwargs.get('id'))
        except Exception as e:
            error_message = {"invalid": "Not found!!"}
            return Response(error_message, status.HTTP_404_NOT_FOUND)
        serializer = StudentBasicInfoSerializer(student_info, context={"request": request})
        return Response(serializer.data, status.HTTP_200_OK)