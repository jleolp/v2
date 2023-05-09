from django.urls import path
from .views import PublicationList, PublicationDetail, PublicationImageList, PublicationImageDetail

urlpatterns = [
    path('publications/', PublicationList.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationDetail.as_view(), name='publication-detail'),
    path('publications/<int:pk>/images/', PublicationImageList.as_view(), name='publication-image-list'),
    path('publications/<int:pk>/images/<int:image_pk>/', PublicationImageDetail.as_view(), name='publication-image-detail'),
]