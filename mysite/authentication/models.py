import uuid
from bson import Binary
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # def save(self, *args, **kwargs):
    #     if not self.pk:  # If the user is being created
    #         # Convert UUID to BSON Binary
    #         self._id = Binary(uuid.uuid4().bytes, 4)
    #
    #     super().save(*args, **kwargs)