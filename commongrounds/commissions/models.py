from django.db import models
from django.urls import reverse


class CommissionType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey(
        CommissionType,
        on_delete=models.CASCADE,
        related_name='commissions',
        null=True
    )
    people_required = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('commissions:detail_view', args=[int(self.id)])
