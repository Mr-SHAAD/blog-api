from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # Auth
    path('register/', views.register_view),
    path('login/', TokenObtainPairView.as_view()),
    
    # Posts
    path('posts/', views.post_list_view),
    path('posts/<int:pk>/', views.post_detail_view),
    
    # Comments
    path('posts/<int:pk>/comment/', views.comment_view),
    
    # Likes
    path('posts/<int:pk>/like/', views.like_view),
]