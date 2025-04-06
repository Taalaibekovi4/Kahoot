from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, QuizViewSet, UserViewSet

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
