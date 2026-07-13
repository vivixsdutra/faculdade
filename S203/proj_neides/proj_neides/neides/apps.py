from django.apps import AppConfig

class NomeDoAppConfig(AppConfig):
    name = 'nome_do_app'

    def ready(self):
        import nome_do_app.signals
        from django.apps import AppConfig


class NeidesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neides'
