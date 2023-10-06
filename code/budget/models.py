from django.db import models
from customers.models import Customer
from django.utils.translation import gettext as _

# Create your models here.


class Budget(models.Model):
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Sent')),
        (3, _('Approved')),
        (4, _('Rejected')),
        (5, _('In Progress')),
        (6, _('Finished')),
        (7, _('Delivered'))
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)
    deadline = models.DateField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description
