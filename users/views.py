"""Users views."""

# Django
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, View
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView

#Mixins
from Plasmotec.mixins import ValidatePermissionRequiredMixin


# Models
from users.models import User

#Forms
from users.forms import *


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('Productos:Fichas_tecnicas')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view"""


class UserListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):

    template_name = 'users/lista_usuarios.html'
    model = User
    permission_required = 'view_user'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    item = i.toJSON()
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['list_url'] = reverse_lazy('users:listado_usuarios')
        context['entity'] = 'Usuarios'
        return context


class UserCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    """Vista para crear las fichas técnicas"""

    model = User
    form_class = UserForm
    permission_required = 'add_user'
    template_name = 'users/crear_usuario.html'
    success_url = reverse_lazy('users:listado_usuarios')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo Usuario'
        context['list_url'] = reverse_lazy('users:listado_usuarios')
        context['entity'] = 'Usuarios'
        context['action'] = 'add'
        return context


class UserUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    """Vista para crear las fichas técnicas"""

    model = User
    form_class = UserForm
    permission_required = 'change_user'
    template_name = 'users/crear_usuario.html'
    success_url = reverse_lazy('users:listado_usuarios')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar usuario'
        context['list_url'] = reverse_lazy('users:listado_usuarios')
        context['entity'] = 'Usuarios'
        context['action'] = 'edit'
        return context


class UserDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    
    model = User
    permission_required = 'delete_user'
    templete_name = 'users/delete.html'
    success_url = reverse_lazy('users:listado_usuarios')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar usuario'
        context['list_url'] = reverse_lazy('users:listado_usuarios')
        context['entity'] = 'Usuarios'
        return context


class UserChangeGroup(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('Produccion:Ordenes_produccion'))


class UserProfileView(LoginRequiredMixin, UpdateView):
    """Vista para crear las fichas técnicas"""

    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('inicio')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save(commit=True)
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de perfil'
        context['list_url'] = reverse_lazy('inicio')
        context['entity'] = 'Perfil'
        context['action'] = 'edit'
        return context


class UserChangePasswordView(LoginRequiredMixin, FormView):
    """Vista para crear las fichas técnicas"""

    model = User
    form_class = PasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = PasswordChangeForm(user=request.user, data= request.POST)
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No ha ingresado a ninguna opción!'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar contraseña'
        context['list_url'] = reverse_lazy('users:login')
        context['entity'] = 'Contraseña'
        context['action'] = 'edit'
        return context