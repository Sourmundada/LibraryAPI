from django.urls import path
from api.views import BookAPIView, BookAPIDetailView

urlpatterns = [
    path('', BookAPIView.as_view()),
    path('<int:pk>/', BookAPIDetailView.as_view()),
]