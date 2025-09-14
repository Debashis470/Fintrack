
# Create your views here.
from rest_framework import viewsets
from .models import Financedata
from .serializers import FinanceDataSerializer

class FinanceDataViewSet(viewsets.ModelViewSet):
    queryset = Financedata.objects.all()
    serializer_class = FinanceDataSerializer
