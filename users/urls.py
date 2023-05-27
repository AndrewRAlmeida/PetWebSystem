from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("minhaconta/", views.minhaconta, name="minhaconta"),
    path("minhaconta/solicitacoes", views.solicitacoes, name="solicitacoes"),
    path("minhaconta/alterar_cadastro", views.alterarcadastro, name="alterarcadastro"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", views.password_reset_request, name="password_reset")
]