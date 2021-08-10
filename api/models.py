from django.db import models

class Email(models.Model):
	title = models.CharField(max_length=64, default="Mail from HOGI.BI")
	subject = models.CharField(max_length=64, default="VISITOR MESSAGE")
	body = models.TextField()
	to = models.TextField()