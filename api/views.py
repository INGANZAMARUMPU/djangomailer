from rest_framework import viewsets
from .serializers import *

class EmailViewset(viewsets.ModelViewSet):
	queryset = Email.objects.filter(id=0)
	serializer_class = EmailSerializer

