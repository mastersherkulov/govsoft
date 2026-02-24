from django.db import models

class Organizations(models.Model):
    org_code = models.IntegerField()
    org_name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)