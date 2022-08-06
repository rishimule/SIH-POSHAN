from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeDoneView,
    PasswordChangeView
)


app_name = 'accounts'

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='accounts/login.html',
                           redirect_authenticated_user=True),
         name='login'),

    path('logout/',
         LogoutView.as_view(),
         name='logout'),

    path('password_change/',
         PasswordChangeView.as_view(
             template_name='accounts/password_change_form.html',
             success_url=reverse_lazy('accounts:password_change_done')
         ),
         name='password_change'),

    path('password_change_done/',
         PasswordChangeDoneView.as_view(
             template_name='accounts/password_change_done.html'
         ),
         name='password_change_done'),

    path('password_reset',
         PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             email_template_name='accounts/password_reset_email.html',
             subject_template_name='accounts/password_reset_subject.txt',
             success_url=reverse_lazy('accounts:password_reset_done')
         ),
         name='password_reset'),

    path('password_reset_done/',
         PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password_reset_<uidb64>_<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html',
             success_url=reverse_lazy('accounts:password_reset_complete')
         ),
         name='password_reset_confirm'),

    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]
