from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT authentication
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
