from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def movie_list(request):
    # Get all movies
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    # Get all seats that are not booked
    available_seats = Seat.objects.filter(is_booked=False)

    # Optionally, filter seats that have not been booked for this movie
    booked_seats = Booking.objects.filter(movie=movie).values_list('seat_id', flat=True)
    available_seats = available_seats.exclude(id__in=booked_seats)

    if not available_seats:
        return render(request, 'bookings/no_seats_available.html', {'movie': movie})

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'available_seats': available_seats
    })

def confirm_booking(self, request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)
    # Handle seat booking logic (mark as booked, etc.)
    seat.is_booked = True
    seat.save()
    return render(request, 'bookings/booking_confirmation.html', {'seat': seat})

def booking_history(request):
    # Get all bookings of the logged-in user
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
