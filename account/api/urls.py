from account.api.views import AccountUserView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', AccountUserView, basename='account')
urlpatterns = router.urls












