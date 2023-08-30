from django.urls import path, include
from product.views import OrganizationAPIView


urlpatterns = [
    path('', OrganizationAPIView.as_view()),

]