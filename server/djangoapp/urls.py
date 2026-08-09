from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("admin/", views.admin_page, name="admin"),
    path("djangoapp/login", views.login_user, name="login"),
    path("djangoapp/logout", views.logout_user, name="logout"),
    path("djangoapp/get_cars", views.get_cars, name="get_cars"),
    path("analyze/<path:text>", views.analyze, name="analyze"),
    path("fetchDealers", views.fetch_dealers, name="fetch_dealers"),
    path("fetchDealers/<str:state>", views.fetch_dealers_by_state, name="fetch_dealers_by_state"),
    path("fetchDealer/<int:dealer_id>", views.fetch_dealer, name="fetch_dealer"),
    path("fetchReviews/dealer/<int:dealer_id>", views.fetch_reviews, name="fetch_reviews"),
]
