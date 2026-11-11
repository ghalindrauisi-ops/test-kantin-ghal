import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kantin_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'Ghalindra'
email = 'ghalindra@ui.ac.id'
password = '123456789ABC'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' berhasil dibuat! Password: {password}")
else:
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    print(f"Superuser '{username}' sudah ada. Password telah di-reset ke: {password}")
