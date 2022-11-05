from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from LaborTools.views import EquipamentosViewSet, MaoDeObraViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'equipamentos', EquipamentosViewSet)
router.register(r'maodeobra', MaoDeObraViewSet)

urlpatterns = [
    path('auth-token/', TokenObtainPairView.as_view()),
    path('auth-refresh-token/', TokenRefreshView.as_view()),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]