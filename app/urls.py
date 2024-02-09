from django.urls import path, include
from app.views import UserRegistrationView,UserLoginView,UserProfileView,UserTaskView
from app.views import UserTasksView



urlpatterns = [
       path("register/", UserRegistrationView.as_view(), name="register-user"),
       path("login/", UserLoginView.as_view(), name="login-user"),
       path("profile/", UserProfileView.as_view(), name="profile"),
       path("tasks/", UserTasksView.as_view(), name="tasks"),
       path("tasks/<str:title>", UserTaskView.as_view(), name="task")
]
