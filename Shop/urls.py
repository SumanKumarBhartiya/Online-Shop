from . import views
from django.urls import path
urlpatterns = [
    path('',views.index, name="ShopHome"),
    path('about/',views.About, name="AboutUs"),
    path('contact/',views.contact, name="ContactUs"),
    path('tracker/',views.Tracker, name="TrackingStatus"),
    path('search/',views.Search, name="Search"),
    path('products/<int:myid>',views.ProductView, name="ProductView"),
    path('checkout/',views.Checkout, name="Checkout"),
]
