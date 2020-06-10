from rest_framework import routers
from cards import views

router = routers.SimpleRouter()
router.register(r'cards', views.CardViewSet)
router.register(r'cards/<int:pk>/', views.CardViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'users/<int:pk>/', views.UserViewSet)

urlpatterns = router.urls


