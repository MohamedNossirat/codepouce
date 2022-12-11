from django.db import models
from accounts.models import CodePouceUser
import uuid


# Create your models here.
class Demande(models.Model):
    owner = models.ForeignKey(
        CodePouceUser,
        on_delete=models.CASCADE,
        related_name='demandes',
        null=True,
        blank=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_rdv = models.DateTimeField(null=True,blank=True)
    description = models.TextField(blank=True, null=True)
    terminee = models.BooleanField(default=False)

    def __str__(self):
        return self.title
