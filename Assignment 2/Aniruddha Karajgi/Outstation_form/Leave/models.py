from django.db import models
from django.core.urlresolvers import reverse
import datetime


class Leave(models.Model):
    name = models.CharField(max_length=100)
    hostel_name = models.CharField(max_length=100)
    departure_date = models.DateField(default=datetime.date.today)
    arrival_date = models.DateField(default=datetime.date.today)
    approval = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('Leave:leave_list_view')

    def __str__(self):
        return self.name + "-" + str(self.departure_date) + "-" + str(self.arrival_date)


