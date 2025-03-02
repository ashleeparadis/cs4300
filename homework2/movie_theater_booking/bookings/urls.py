from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet, SeatViewSet, BookingViewSet, 
    movie_list, book_seat, booking_history, book_seat
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename = 'movie')
router.register(r'seats', SeatViewSet, basename = 'seat')
router.register(r'bookings', BookingViewSet, basename = 'booking')

urlpatterns = [
    #API endpoints
    path('api/', include(router.urls)), 

    #Frontend URLs for rendering templates
    path('movies/', movie_list, name='movie_list'),
    path('seat-booking/', book_seat, name='book_seat'),
    path('booking-history/', booking_history, name='booking_history'),
    path('book_seat/<int:movie_id>', book_seat, name='book_seat'),

    path('', movie_list, name='home'),
]