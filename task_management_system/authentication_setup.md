# Authentication Setup

## Overview
This API uses Django REST Framework's built-in authentication system with token-based authentication. 

## Steps to Test
1. **Generate a Token**
   - Run the following command:
     ```bash
     python manage.py drf_create_token <username>
     ```
   - Replace `<username>` with your existing username. Save the token.

2. **Test the API**
   - Use the `/api/protected/` endpoint.
   - Add an `Authorization` header with the format:
     ```
     Token <your_token>
     ```
   - Example cURL command:
     ```bash
     curl -X GET http://127.0.0.1:8000/api/protected/ \
         -H "Authorization: Token <your_token>"
     ```

3. **Expected Response**
   If authenticated successfully:
   ```json
   {
       "message": "Hello, <username>! Welcome to the protected endpoint."
   }
