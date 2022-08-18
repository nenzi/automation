from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Automation(models.Model):
    STATUS = [
        ("pending", "pending"),
        ("running", "running"),
        ("completed", "completed"),
    ]

    TRIGGER = (
        ("opt_in", "opt_in"),
        ("time_trigger", "time_trigger"),
        ("removed_from_list", "removed_from_list"),
        ("purchase_activity", "purchase_activity"),
        ("list_trigger", "list_trigger"),
        ("page_visited_trigger", "page_visited_trigger"),
        ("register_seminar_trigger", "register_seminar_trigger"),
    )
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    trigger = models.CharField(choices=TRIGGER, max_length=200, default="opt_in")
    conditions = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    actions = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=200, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
