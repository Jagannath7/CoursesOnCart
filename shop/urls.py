
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    # path('<int:prod_id>', views.detail, name='detail'),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:myid>", views.productView, name="ProductView"),
]
