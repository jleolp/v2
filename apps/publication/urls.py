from django.urls import path
from apps.publication.views import *
urlpatterns = [
    path('publications/', PublicationList.as_view(), name='publication-list'),
    path('publications/<int:pk>/', PublicationDetail.as_view(), name='publication-detail'),
    path('publications/<int:pk>/images/', PostImageList.as_view(), name='publication-image-list'),
    path('publications/<int:pk>/images/<int:image_pk>/', PostImageDetail.as_view(), name='publication-image-detail'),
] 