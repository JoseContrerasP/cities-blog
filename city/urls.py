from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("city/<int:id>", views.get_city, name="city"),
    path(
        "city/<int:id>/create_new_comment",
        views.create_new_comment,
        name="create_new_comment",
    ),
    path(
        "city/<int:id_city>/<int:id_comment>/like_comment",
        views.like_comment,
        name="like_comment",
    ),
    path("city/create", views.create_new_city, name="create_new_city"),
    path("city/<int:city_id>/delete", views.delete_city, name="delete_city"),
    path("city/<int:city_id>/edit", views.edit_city, name="edit_city"),
    path("city/my", views.my_cities, name="my_cities"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
]
