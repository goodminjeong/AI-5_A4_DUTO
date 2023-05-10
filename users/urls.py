from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('login/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('<int:user_id>/', views.ProfileView.as_view(), name='profile_view'),
    path('<int:user_id>/follow/', views.FollowView.as_view(), name='follow_view'),
    path('<int:user_id>/myposts/', views.MypostsView.as_view(), name='myposts_view'),
    path('<int:user_id>/likes/', views.LikesView.as_view(), name='likes_view'),
]