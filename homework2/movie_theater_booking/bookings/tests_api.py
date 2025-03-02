from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking

class APITestMovies (APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="A test description for movie api",
            release_date="2025-02-25",
            duration=140
        )

    def test_fetch_movie(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0, "No movies found")
        self.assertEqual(response.data[0]["title"], "API Test Movie")

class APITestSeat(APITestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_num = "D3")

    def test_fetch_seat(self):
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class APITestBooking(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="apiusertest", password="password1234")

        self.movie = Movie.objects.create(
            title="API Booking Movie",
            description="Test description for api booking movie.",
            release_date="2025-02-24",
            duration=120
        )

        self.seat = Seat.objects.create(seat_num="B5")

    def test_create_booking(self):
        self.client.login(username="apiusertest", password="password1234") 
        data = {"movie": self.movie.id, "seat": self.seat.id, "user": self.user.id}
        response = self.client.post("/api/bookings/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)