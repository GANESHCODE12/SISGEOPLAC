# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms.models import model_to_dict
from crum import get_current_request



class User(AbstractUser):
    """User model."""

    email = models.EmailField(
        unique=True,
        verbose_name='Email')

    password = models.CharField(
        max_length=100,
        verbose_name='Contraseña'
    )

    first_name = models.CharField(
        max_length=100,
        verbose_name='Nombres'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Apellidos'
    )

    is_admin = models.BooleanField(
        default=False,
        verbose_name='Administrador'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de modificación'
    )

    class Meta:
        """Configuración del modelo"""

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuarios'
        ordering = ['-id']

    def toJSON(self):
        item = model_to_dict(
            self,
            exclude=[
                'password',
                'last_login',
                'user_permissions'
            ]
        )
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name}for g in self.groups.all()]
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass
