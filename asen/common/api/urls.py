from django.urls import path
from asen.common.api.views import GenderListView

urlpatterns = [
    path("genders/", GenderListView.as_view(), name="gender_list")
]
