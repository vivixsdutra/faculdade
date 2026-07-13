import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj_neides.settings')
django.setup()

# Criar usuário cliente
if not User.objects.filter(username='cliente').exists():
    client_user = User.objects.create_user('cliente', 'cliente@example.com', '141251')
    client_user.save()
    print("Usuário cliente criado com sucesso.")