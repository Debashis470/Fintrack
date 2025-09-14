from decimal import Decimal
from django.db import models

class Financedata(models.Model):
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_expense = models.DecimalField(max_digits=10, decimal_places=2)
    goal_target = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sip_investment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sip_rate = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("12.00"))  # make this Decimal
    sip_years = models.IntegerField(default=1)

    def savings(self):
        return self.monthly_income - self.monthly_expense

    def is_loan_eligible(self):
        return self.monthly_income >= 2 * self.monthly_expense

    def sip_estimated_return(self):
        r = self.sip_rate / Decimal("100.0") / Decimal("12.0")
        n = self.sip_years * 12
        fv = self.sip_investment * (((Decimal(1) + r) ** n - 1) / r) * (Decimal(1) + r)
        return round(fv, 2)
