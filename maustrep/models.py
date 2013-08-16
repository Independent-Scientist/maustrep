from django.db import models
from django.contrib.auth.hashers import make_password

class Trap(models.Model):
    # Descriptor for the trap, the name you want it to have on the url
    descriptor = models.CharField(max_length="256", blank=False)
    # pass
    password = models.CharField(max_length="256", blank=False)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)



class TrapRecord(models.Model):
    # trap ref
    trap = models.ForeignKey(Trap)
    #ip adress
    ip_addr = models.CharField(max_length="128", blank=False)
    # date/time
    datetime = models.DateTimeField(auto_now=True)

