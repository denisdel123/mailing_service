from django.urls import path

from usersApp.apps import UsersappConfig
from usersApp.views import LoginView, LogoutView, RegistrationView, UserUpdateView, UserListView, UserDetailView, \
    UserDeleteView, forgot_password, PasswordChange, email_confirm, send_code

app_name = UsersappConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('list/', UserListView.as_view(), name='list'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),



    path('forgot_password/', forgot_password, name='forgot_pass'),
    path('change_password/', PasswordChange.as_view(), name='change_pass'),
    path('email_confirm/', email_confirm, name='email_confirm'),
    path('send_code/', send_code, name='send_code'),
]