from django.urls import path, include
from .models import Genre
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as v
router = DefaultRouter()

router.register(r'Author', views.AuthorViewSet)
router.register(r'Book', views.BookViewSet)
router.register(r'Genre', views.GenreViewSet)
router.register(r'BookInstance', views.BookInstanceViewSet)
router.register(r'User', views.UserViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('api', include(router.urls)),
    path('count_books', views.count_books, name="count"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Book_Create', views.BookCreate.as_view(), name='Book_Create'),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='api-token-auth'),
    path('NewAPI', views.NewAPI.as_view(), name='NewAPI'),
    path('Scenario1', views.Scenario1.as_view(), name='Scenario1'),
    path('Scenario2', views.Scenario2.as_view(), name='Scenario2'),
    path('Scenario3', views.Scenario3.as_view(), name='Scenario3'),
    path('Scenario4', views.Scenario4.as_view(), name='Scenario4'),
    path('Scenario5', views.Scenario5.as_view(), name='Scenario5'),
    path('Scenario9', views.Scenario9.as_view(), name='Scenario9'),

]
