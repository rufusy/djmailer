from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SubscriberViewSet

app_name = 'api'

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)
urlpatterns = router.urls


