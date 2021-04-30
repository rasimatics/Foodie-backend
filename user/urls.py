from django.urls import path
from .views import Register, Login, RefreshToken, GetProfile, EditProfile

urlpatterns = [
    path("sign-up/", Register.as_view(), name="signup"),
    path('sign-in/', Login.as_view(), name="signin"),
    path("refresh-token/", RefreshToken.as_view(), name="refresh-token"),

    path('profile/', GetProfile.as_view(), name="profile"),
    path('edit-profile/<int:id>/', EditProfile.as_view(), name="edit-profile")
]
