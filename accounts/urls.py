# accounts/urls.py
from django.urls import path
# from django.conf.urls import url
from . import views # from current directory to look for views file
from django.contrib.auth.decorators import login_required
from .decorators import anonymous_required
from django.contrib.auth.views import LoginView

app_name = 'accounts'
# has to be called urlpatterns
urlpatterns = [
    path('signup/', anonymous_required(view_function=views.SignUp.as_view(), redirect_to="/"), name='signup'),
    path('profile/edit/', login_required(views.edit_profile,  login_url="/accounts/login/"), name='edit_profile'),
    path('profile/', login_required(views.GetAuthorProfile, login_url="/accounts/login/"), name='profile'),
    path('friends/author/<str:author_id>/', views.AuthorProfile().as_view()),
    path('login/', anonymous_required(LoginView.as_view(template_name='registration/login.html'), redirect_to="/"), name="login"),
    path('friends/', login_required(views.friendlistpage,login_url="/accounts/login/"), name='friendpage'),
    path(r'getFriendrequest/', login_required(views.getFriendRequest,login_url="/accounts/login/"), name='friendrequestpage'),
]
