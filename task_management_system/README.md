# Task Management System

## Setup Instructions

1. Clone this repository to your local machine.
2. Navigate to the `task_management_system` directory.
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```
   python manage.py migrate
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Open your browser and go to `http://127.0.0.1:8000`.

## Features
- User authentication
- Task creation and management
- Admin panel for managing tasks and users
