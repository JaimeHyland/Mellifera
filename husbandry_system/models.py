from django.db import models

class HusbandrySystem(models.Model):
    name = models.TextField(max_length=254)
    box_height_mm = models.PositiveIntegerField(default=0)
    box_depth_mm = models.PositiveIntegerField(default=0)
    box_width_mm = models.PositiveIntegerField(default=0)
    frame_height_mm = models.PositiveIntegerField(default=0)
    frame_depth_mm = models.PositiveIntegerField(default=0)
    frame_width_mm = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
