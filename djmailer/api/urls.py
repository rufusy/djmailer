from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SubscriberViewSet, login

app_name = 'api'

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)
#urlpatterns = router.urls

urlpatterns = [
    path('login/', login, name="login"),
]

urlpatterns += router.urls


