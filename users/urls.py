# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    path(
        route='logout/', 
        view=views.LogoutView.as_view(), 
        name='logout'
    ),
    path(
        route='listado_usuarios/', 
        view=views.UserListView.as_view(), 
        name='listado_usuarios'
    ),
    path(
        route='nuevo_usuario/', 
        view=views.UserCreateView.as_view(), 
        name='nuevo_usuario'
    ),
    path(
        route='actualizar_usuario/<int:pk>/', 
        view=views.UserUpdateView.as_view(), 
        name='actualizar_usuario'
    ),
    path(
        route='eliminar_usuario/<int:pk>/', 
        view=views.UserDeleteView.as_view(), 
        name='eliminar_usuario'
    ),
    path(
        route='change/group/<int:pk>/', 
        view=views.UserChangeGroup.as_view(), 
        name='user_change_group'
    ),
    path(
        route='Perfil/', 
        view=views.UserProfileView.as_view(), 
        name='Perfil'
    ),
    path(
        route='Cambiar/Contraseña/', 
        view=views.UserChangePasswordView.as_view(), 
        name='Cambiar_contraseña'
    ),
    path(
        route='reset-password/', 
        view=views.ResetPasswordView.as_view(), 
        name='reset-password'
    ),
    path(
        route='change-password/<str:token>', 
        view=views.ChangePasswordView.as_view(), 
        name='change-password'
    ),

]
