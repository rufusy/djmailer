from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SubscriberViewSet, login
from rest_framework_jwt.views import obtain_jwt_token


app_name = 'api'

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)
#urlpatterns = router.urls

urlpatterns = [
    path('login/', login, name="login"),
    path('jwt-auth/', obtain_jwt_token),
]

urlpatterns += router.urls


