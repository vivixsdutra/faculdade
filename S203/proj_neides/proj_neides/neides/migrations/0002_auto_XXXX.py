from django.db import migrations
from django.contrib.auth.models import User

def create_users(apps, schema_editor):
    # Criar usuário admin
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'neides123')
        admin_user.save()

    # Criar usuário cliente
    if not User.objects.filter(username='cliente').exists():
        client_user = User.objects.create_user('cliente', 'cliente@example.com', '141251')
        client_user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('neides', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
    ]