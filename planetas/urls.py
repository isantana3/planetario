from django.urls import path
from .views import list_planetas, create_planeta, update_planeta, delete_planeta, detail_planeta

app_name = "planetario"

urlpatterns = [
    path('', list_planetas, name='list_planetas'),
    path('detail/<int:id>/', detail_planeta, name='detail_planeta' ),
    path('new', create_planeta , name='create_planeta'),
    path('update/<int:id>/', update_planeta, name='update_planeta'),
    path('delete/<int:id>/', delete_planeta, name='delete_planeta'),
]
