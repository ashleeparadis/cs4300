from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import (
    MovieViewSet, SeatViewSet, BookingViewSet, 
    movie_list, book_seat, booking_history, confirm_booking, register, user_login,
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename = 'movie')
router.register(r'seats', SeatViewSet, basename = 'seat')
router.register(r'bookings', BookingViewSet, basename = 'booking')

urlpatterns = [
    #API endpoints
    path('api/', include(router.urls)), 

    #Frontend URLs for rendering templates
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('movies/', movie_list, name='movie_list'),
    path('booking-history/', booking_history, name='booking_history'),
    path('book_seat/<int:movie_id>/', book_seat, name='book_seat'),
    path('confirm_booking/<int:movie_id>/', confirm_booking, name='confirm_booking'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', movie_list, name='home'),
]