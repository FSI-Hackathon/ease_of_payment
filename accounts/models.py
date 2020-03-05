from __future__ import unicode_literals
from django.db import models
import uuid # access to uuid for generating reference id
from django.contrib.auth.models import User

User._meta.local_fields[4].__dict__['_unique'] = True
User._meta.local_fields[4].__dict__['_required'] = True

class Profile(models.Model):
	"""this class is responsible for the profile of each user in the website."""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profilephoto = models.ImageField(null=True)
	reference_id = models.UUIDField(max_length=50, null=False, blank=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	class Meta:
		unique_together = ('reference_id',)

		#making reference key unique will allow each user to have his or her own key unique to him or her.

# Create your models here.
