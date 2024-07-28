# expenses/views.py

from rest_framework import generics
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddExpenseView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class RetrieveUserExpensesView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Expense.objects.filter(user_id=user_id)

class RetrieveOverallExpensesView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# expenses/views.py

import csv
from django.http import HttpResponse
from .models import Expense

class DownloadBalanceSheetView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        expenses = Expense.objects.filter(user_id=user_id)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="balance_sheet_{user_id}.csv"'

        writer = csv.writer(response)
        writer.writerow(['Description', 'Amount', 'Date', 'Split Method'])
        for expense in expenses:
            writer.writerow([expense.description, expense.amount, expense.date, expense.get_split_method_display()])

        return response
