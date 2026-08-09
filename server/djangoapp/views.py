from django.http import JsonResponse
from django.shortcuts import render

from .dealer_data import DEALERS

REVIEWS = [{
    "id": 1,
    "name": "root",
    "dealership": "Best Cars Dealership - Wichita",
    "review": "Fantastic services",
    "purchase": True,
    "car_make": "Toyota",
    "car_model": "Camry",
    "car_year": 2024,
    "purchase_date": "2024-06-15",
}]

CARS = [
    {"Make": "Toyota", "Model": "Camry"}, {"Make": "Honda", "Model": "Accord"},
    {"Make": "Ford", "Model": "Mustang"}, {"Make": "Chevrolet", "Model": "Malibu"},
    {"Make": "Nissan", "Model": "Altima"}, {"Make": "BMW", "Model": "3 Series"},
    {"Make": "Mercedes-Benz", "Model": "C-Class"}, {"Make": "Audi", "Model": "A4"},
    {"Make": "Hyundai", "Model": "Sonata"}, {"Make": "Kia", "Model": "K5"},
    {"Make": "Subaru", "Model": "Outback"}, {"Make": "Mazda", "Model": "CX-5"},
    {"Make": "Volkswagen", "Model": "Jetta"}, {"Make": "Lexus", "Model": "RX"},
    {"Make": "Volvo", "Model": "XC60"},
]


def home(request):
    return render(request, "index.html", {"dealers": DEALERS})


def about(request):
    return render(request, "About.html")


def contact(request):
    return render(request, "Contact.html")


def admin_page(request):
    return render(request, "admin.html")


def login_user(request):
    return JsonResponse({"userName": "root", "status": "Authenticated"})


def logout_user(request):
    return JsonResponse({"userName": ""})


def get_cars(request):
    return JsonResponse({"CarModels": CARS})


def analyze(request, text):
    return JsonResponse({"sentiment": "positive" if "fantastic" in text.lower() else "neutral"})


def fetch_dealers(request):
    return JsonResponse(DEALERS, safe=False)


def fetch_dealers_by_state(request, state):
    return JsonResponse([dealer for dealer in DEALERS if dealer["state"].lower() == state.lower()], safe=False)


def fetch_dealer(request, dealer_id):
    dealer = next((item for item in DEALERS if item["id"] == dealer_id), DEALERS[0])
    return JsonResponse(dealer)


def fetch_reviews(request, dealer_id):
    return JsonResponse(REVIEWS, safe=False)
