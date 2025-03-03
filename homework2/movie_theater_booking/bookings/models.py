from django.db import models
from django.contrib.auth.models import User

#Movie class to define title, description, release date, and length of movie
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title

#Seat class to define the seat number and whether or not the seat is available to buy
class Seat(models.Model):
    seat_num = models.CharField(max_length=30, unique=True)
    is_booked = models.BooleanField(default=False)
    

    def __str__(self):
        return f"Seat {self.seat_num}: {'Booked' if self.is_booked else 'Available'}"

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seat {self.seat.seat_num}"