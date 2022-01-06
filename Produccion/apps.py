from django.apps import AppConfig


class ProduccionConfig(AppConfig):
    """production application settings"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Produccion'
    verbose_name = 'Producción'
