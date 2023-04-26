from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from asen.users.api.views import UserViewSet
from asen.patients.api.views import PatientViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()
    
router.register("users", UserViewSet)
router.register("patients", PatientViewSet)


app_name = "api"
urlpatterns = router.urls
