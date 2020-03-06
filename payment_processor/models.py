from __future__ import unicode_literals
from django.db import models
from accounts.models import Profile
import uuid # access to uuid for generating reference id
from django.contrib.auth.models import User


class Transaction(models.Model):
	"""this is responsible for all the transactions in the platform"""
	receiver = models.ForeignKey(User, on_delete=models.CASCADE)
	sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
	transaction_id = models.UUIDField(null=False, default=uuid.uuid4)
	amount = models.DecimalField(decimal_places=2, max_digits=15)
	verified = models.BooleanField(default=False)

	class Meta:
		unique_together = ('transaction_id',)
	

		#making transaction id unique will allow each transaction to have a unique key to it.

# Create your models here.
