import uuid
from django.db import models, transaction

# Create your models here.
class Wallet(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    balance = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)

    def deposit(self, amount):
        with transaction.atomic:
            self.balance += amount
            self.save()

    def withdraw(self, amount):
        with transaction.atomic():
            if self.balance >= amount:
                self.balance -= amount
                self.save()
            else:
                raise ValueError('Insufficient funds')