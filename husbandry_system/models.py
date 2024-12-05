from django.db import models

class HusbandrySystem(models.Model):
    name = models.CharField(max_length=100)
    box_length_mm = models.PositiveIntegerField(default=0)
    box_width_mm = models.PositiveIntegerField(default=0)
    depth_deep_mm = models.PositiveIntegerField(null=True, blank=True)
    depth_medium_mm = models.PositiveIntegerField(null=True, blank=True)
    depth_shallow_mm = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
