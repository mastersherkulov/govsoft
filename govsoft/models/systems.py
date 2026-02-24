from django.db import models
from .organizations import Organizations

SYSTEM_TYPE = [
    ("internal", "Internal"),
    ("external", "External"),
    ("public", "Public"),
    ("private", "Private"),
]

class Systems(models.Model):
    org_id = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    system_type = models.CharField(max_length=250, choices=SYSTEM_TYPE)
    system_name = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    