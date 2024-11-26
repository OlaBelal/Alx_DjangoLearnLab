from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

# Registration View
def register(request):
    """
    Handle user registration using Django's built-in UserCreationForm.
    Automatically logs in the user upon successful registration.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Helper function to check user role
def check_role(role):
    """
    Returns a role-checking function for use with @user_passes_test.
    """
    def role_checker(user):
        # Ensure the user is authenticated and their role matches the required role
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return role_checker


# Role-Specific Views
@user_passes_test(check_role('Admin'))
def admin_view(request):
    """
    View accessible only to users with the 'Admin' role.
    """
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})


@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    """
    View accessible only to users with the 'Librarian' role.
    """
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})


@user_passes_test(check_role('Member'))
def member_view(request):
    """
    View accessible only to users with the 'Member' role.
    """
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Test functions for roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
