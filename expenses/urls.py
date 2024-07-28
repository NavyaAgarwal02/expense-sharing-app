# expenses/urls.py

from django.urls import path
from .views import CreateUserView, RetrieveUserView, AddExpenseView, RetrieveUserExpensesView, RetrieveOverallExpensesView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('users/<int:pk>/', RetrieveUserView.as_view(), name='retrieve-user'),
    path('expenses/', AddExpenseView.as_view(), name='add-expense'),
    path('expenses/user/<int:user_id>/', RetrieveUserExpensesView.as_view(), name='retrieve-user-expenses'),
    path('expenses/', RetrieveOverallExpensesView.as_view(), name='retrieve-overall-expenses'),
]

# expenses/urls.py

from .views import DownloadBalanceSheetView

urlpatterns += [
    path('expenses/user/<int:user_id>/download/', DownloadBalanceSheetView.as_view(), name='download-balance-sheet'),
]
