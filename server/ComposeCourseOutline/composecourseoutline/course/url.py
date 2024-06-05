from django.contrib import admin
from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('majors', views.MajorViewSet)
router.register('categories', views.CategoryViewSet)
router.register('courses', views.CourseViewSet)
router.register('outlines', views.OutlineViewSet)
router.register('users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls)
]
