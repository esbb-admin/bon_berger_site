from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
User = get_user_model()
for u in User.objects.all():
    print(f"Username: {u.username} — Email: {u.email}— Password: {u.set_password}") 

