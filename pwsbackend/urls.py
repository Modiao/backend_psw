from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin

from psw.views import *

urlpatterns = [
     path('admin/', admin.site.urls),
     path('api/token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'), 
     path('api/token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
     path('api/exercices/', ExerciceAPIView.as_view(), name='exercices-list'),
     path('api/exercices/<int:id>/', ExerciceRudView.as_view(), name='exercices-rud'),
     path('api/courses/', CourseAPIView.as_view(), name='courses-list'),
     path('api/courses/<int:id>/', CourseRudView.as_view(), name='courses-rud'),
     path('api/corrections/', CorrectionAPIView.as_view(), name='corrections-list'),
     path('api/corrections/<int:id>/', CorrectionRudView.as_view(), name='corrections-rud'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
