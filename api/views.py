from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *

class EmailViewset(viewsets.ModelViewSet):
	queryset = Email.objects.filter(id=0)
	serializer_class = EmailSerializer

	def create(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = serializer.data
		send_mail(
			subject = data.get("subject"),
			message = "",
			from_email = "HOGI.BI <forward@hogi.bi>",
			recipient_list = data.get("to"),
			fail_silently = False,
			html_message = data.get("body"),
		)
		email:Email = Email(
			title = data.get("title"),
			subject = data.get("subject"),
			body = data.get("body"),
			to = ",".join(data.get("to"))
		)
		email.save()
		serializer = EmailOutSerializer(email)
		return Response(serializer.data, 201)