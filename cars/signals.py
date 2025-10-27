from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
#from cars.models import Car, CarInventory

@receiver(pre_save, sender='cars.Car')
def car_pre_save(sender, instance, **kwargs):
    pass        