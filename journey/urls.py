from django.urls import path
from . import views
from .views import TripListView, TripDetailView, TripCreateView,TripUpdateView,TripDeleteView,AllTripsListView

urlpatterns = [
    path('', TripListView.as_view(),name = 'journey-home'),
    path('all', AllTripsListView.as_view(),name = 'journey-all'),
    path('trip/<int:pk>/', TripDetailView.as_view(),name = 'trip-detail'),
    path('trip/<int:pk>/update/',TripUpdateView.as_view(),name = 'trip-update'),
    path('trip/<int:pk>/delete/',TripDeleteView.as_view(),name = 'trip-delete'),
    path('trip/new/', TripCreateView.as_view(),name = 'trip-create'),
    path('about/', views.about,name = 'journey-about'),
]