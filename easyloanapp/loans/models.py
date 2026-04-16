from django.db import models
from django.contrib.auth.models import User

class Loan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    term_months = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    next_payment_date = models.DateField()

    def progress(self):
        paid = self.amount - self.remaining_balance
        return int((paid / self.amount) * 100)