from django.urls import path,include

urlpatterns = [
    path('/auth', include('apps.auth.urls')),
    path('/cars', include('apps.car.urls')),
    path('/auto_parks', include('apps.auto_park.urls')),
    path('/users', include('apps.user.urls')),

]
