# Daily Expenses Sharing Application

## Setup Instructions

1. Clone the repository. `https://github.com/NavyaAgarwal02/expense-sharing-app`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## API Endpoints

### User Endpoints

- `POST /api/users/` - Create a user.
- `GET /api/users/<id>/` - Retrieve user details.

### Expense Endpoints

- `POST /api/expenses/` - Add expense.
- `GET /api/expenses/user/<user_id>/` - Retrieve individual user expenses.
- `GET /api/expenses/` - Retrieve overall expenses.
- `GET /api/expenses/user/<user_id>/download/` - Download balance sheet.

