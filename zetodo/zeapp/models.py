import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _



class TaskModel(models.Model):
    PRIORITIES = [
        (0, "Faible"),
        (1, "Moyen"),
        (2, "Elevé"),
        (3, "Critique"),
    ]
    STATUS =  [
        (0, "A faire"),
        (1, "En cours"),
        (2, "Terminé"),
        (3, "Annulé"),
        (4, "En attente"),
        (5, "En pause"),
        (6, "En attente de validation")
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"),max_length=100)
    memo = models.TextField(_("Description"),null=True,blank=True)
    priority = models.IntegerField(_("Priority"), choices=PRIORITIES,null=True,blank=True)
    duedate = models.DateField(_("Due date"),null=True,blank=True)
    status = models.IntegerField(_("Status"), choices=STATUS,null=True,blank=True)
    created_date = models.DateTimeField(_("Created date"), editable=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-priority"]
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks") 