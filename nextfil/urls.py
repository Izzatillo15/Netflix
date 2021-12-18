from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from nextapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from nextapp.views import ActorViewSet, MovieViewSet
from drf_yasg.views import get_schema_view

doc_view = get_schema_view(
    openapi.Info(
        title="Clone app for Netflix",
        default_version='v1',
        description="(REST API) Clone of Netflix using Django Rest Framework",
        contact=openapi.Contact("Izzatillo Olimjonov <olimjonovizzatillo95@gmail.com>")

    ),
    public=True,
    permission_classes=(AllowAny,),

)




router = DefaultRouter()
router.register('actor', ActorViewSet)
router.register('movie',  MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('doc/',doc_view.with_ui("swagger",cache_timeout=0),name="swagger_doc"),
    path('redoc/',doc_view.with_ui("redoc",cache_timeout=0),name="redoc_doc"),
]