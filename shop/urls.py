
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    # path('<int:prod_id>', views.detail, name='detail'),
    path("products/<int:myid>", views.productView, name="ProductView"),
]
