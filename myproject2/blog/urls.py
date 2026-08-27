from . import views
from django.urls import path,re_path

urlpatterns = [
    path("post/<int:post_id>/", views.showpost, name="showpost"),
    path("user/<str:username>/", views.user_details, name="user_details"),
    path("articles/<int:year>/<int:month>/<int:day>/", views.article_use, name="article_use"),
   # re_path(r"^article/(?P<year>[0-9]{4})/$", views.article_details, name="article_details"),
]