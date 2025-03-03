from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    seats = Seat.objects.all()

    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

@login_required
def confirm_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        seat_num = request.POST.get('seat_num')

        # Get the seat object based on the seat number entered by the user
        seat = get_object_or_404(Seat, seat_num=seat_num)

        if seat.is_booked:
            # If the seat is already booked, send a message to the template
            return render(request, 'bookings/seat_booking.html', {
                'movie': movie,
                'seats': Seat.objects.all(),
                'error_message': 'Seat is already booked.'
            })

        # Mark the seat as booked
        seat.is_booked = True
        seat.save()

        # Create a booking object
        Booking.objects.create(movie=movie, seat=seat, user=request.user, booking_date=timezone.now())

        # After booking, redirect to the booking history page
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': Seat.objects.all()})

@login_required
def booking_history(request):

    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            messages.success(request, 'Registration successful.')
            return redirect('movie_list')  # Redirect to the movie list
    else:
        form = UserCreationForm()
    return render(request, 'bookings/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('movie_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'bookings/login.html', {'form': form})

