from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking

class MovieModelTest(TestCase):
    #Function to create a mock movie
    def setUp(self):
        self.movie = Movie.objects.create(
            title = "Test Movie",
            description = "Test Description of Movie",
            release_date = "2025-02-26",
            duration = 110
        )

    #Test function that verifies movie is correctly created
    def test_movie(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.description, "Test Description of Movie")
        self.assertEqual(self.movie.duration, 110)

class TestSeatModel(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_num = "B9")

    def test_seat(self):
        self.assertEqual(self.seat.seat_num, "B9")
        self.assertEqual(self.seat.is_booked, False)

class TestBookingModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = "usertester", password = "1234")
        self.movie = Movie.objects.create(
            title = "Test movie 2",
            description = "Description for test movie 2",
            release_date = "2025-02-28",
            duration = 90
        )

        self.seat = Seat.objects.create(seat_num = "A7")
        self.booking = Booking.objects.create(
            user = self.user,
            movie = self.movie,
            seat = self.seat
        )

    #Test function to verify a booking model is created correctly
    def test_booking(self):
        self.assertEqual(self.booking.user.username, "usertester")
        self.assertEqual(self.booking.movie.title, "Test movie 2")
        self.assertEqual(self.booking.seat.seat_num, "A7")