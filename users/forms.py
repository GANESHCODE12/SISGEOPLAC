#Django
from django.forms import *

#Models
from users.models import *



class UserForm(ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'groups'
        ]
        exclude = [
            'user_permissions',
            'last_login',
            'date_joined',
            'is_superuser',
            'is_active',
            'is_staff'
        ]
        widgets = {
            'password': PasswordInput(
                render_value=True
            ),
            'groups': SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%',
                    'multiple': 'multiple'
                }
            ),
        }
    
    def save(self, commit:True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)  
                u.save()
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class UserProfileForm(ModelForm):
    """Modelo para la creación de fichas"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        """Configuración del formulario"""

        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]
        exclude = [
            'user_permissions',
            'last_login',
            'date_joined',
            'is_superuser',
            'is_active',
            'is_staff'
            'groups'
        ]
        widgets = {
            'password': PasswordInput(
                render_value=True
            ),
            'groups': SelectMultiple(
                attrs={
                    'class': 'form-control select2',
                    'style': 'width: 100%',
                    'multiple': 'multiple'
                }
            ),
        }
    
    def save(self, commit:True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)  
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data