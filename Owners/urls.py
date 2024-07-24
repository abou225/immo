from django.urls import path
from Owners.views import index, show, create, update, delete


urlpatterns = [
    path("index/", index, name='o-list'),
    path("show/<int:id>", show, name="o-show"),
    path("create/", create, name='o-create'),
    path("update/<int:id>", update, name='o-update'),
    path("delete/<int:id>", delete, name='o-delete'),
]