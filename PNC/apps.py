from django.apps import AppConfig


class PncConfig(AppConfig):
    """Non-conforming application settings"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PNC'
    verbose_name = 'Producto No Conforme'
