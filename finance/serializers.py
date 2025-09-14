from rest_framework import serializers
from .models import Financedata


class FinanceDataSerializer(serializers.ModelSerializer):
    savings = serializers.SerializerMethodField()
    loan_eligibility = serializers.SerializerMethodField()
    sip_estimated_return = serializers.SerializerMethodField()

    class Meta:
        model = Financedata
        fields = [
            "monthly_income", "monthly_expense", "goal_target",
            "sip_investment", "sip_rate", "sip_years",
            "savings", "loan_eligibility", "sip_estimated_return"
        ]

    def get_savings(self, obj):
        return obj.savings()

    def get_loan_eligibility(self, obj):
        return "Yes" if obj.is_loan_eligible() else "No"

    def get_sip_estimated_return(self, obj):
        return obj.sip_estimated_return()
