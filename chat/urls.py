#url en la cual se crea y otro e el que se muestra
from django.urls import path
from . import views


urlpatterns =[
    path("messages/", view=views.get_messages, name="get-messages"),
    path("messages/create/", view=views.create_message, name="create-message"),
    path("authors/<int:author_id>/profile_picture", view=views.update_profile_picture, name="update-profile-picture"),
    path("authors/<str:username>/", view=views.get_author_by_username, name="get-author-by-username")
]