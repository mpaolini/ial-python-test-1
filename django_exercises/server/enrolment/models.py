from django.db import models

class student(models.Model):
	name = models.TextField()
	surname = models.TextField()