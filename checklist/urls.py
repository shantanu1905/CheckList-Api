from django.contrib import admin
from django.urls import path , include
from  checklist.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/checklist/', CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/', ChecklistUpdateDelete.as_view()),
    path('api/checklistItem/create/', CheckListItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>/', CheckListItemAPIView.as_view()),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]



