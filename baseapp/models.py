from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

#CustomUser = settings.AUTH_USER_MODEL



class BaseModel(models.Model):
    created_at = models.DateField(blank=False)
    updated_at = models.DateField(auto_now=False)
    # created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_created_by",
    #                                null=True, blank=True, on_delete=models.SET_NULL)
    # updated_by = models.ForeignKey(User, related_name='%(app_label)s_%(class)s_updated_by',
    #                                null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


