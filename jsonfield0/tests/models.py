
from django.db import models

from qjsonfield import JSONField, JSONAwareManager

class JsonModel(models.Model):
    code = models.CharField( blank=False, null=False, max_length=20 )
    info = JSONField(default={})

    objects = JSONAwareManager(json_fields = ['info'])

