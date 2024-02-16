from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from crum import get_current_request


class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('diagrama-gantt')
        return self.url_redirect

    def dispatch(self, request, *args, **kwargs):
        request = get_current_request()
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if 'group' in request.session:
            group = request.session['group']
            if group.permissions.filter(codename=self.permission_required):
                return super().dispatch(request, *args, **kwargs)
        messages.error(request, 'No tiene permiso para ingresar a este módulo')
        return HttpResponseRedirect(self.get_url_redirect())