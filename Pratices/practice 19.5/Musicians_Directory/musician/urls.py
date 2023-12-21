
from django.urls import path
from . import views


urlpatterns = [
    # path('add/', views.add_musician , name='add_musician'),
    path('add/', views.AddMusicianView.as_view() , name='add_musician'),
    # path('edit/<int:id>', views.edit_musician, name='edit_musician'),
    path('edit/<int:id>', views.EditMusicianView.as_view(), name='edit_musician'),
    # path('delete/<int:id>', views.delete_musician, name='delete_musician'),
    path('delete/<int:id>', views.DeletemusicianView.as_view(), name='delete_musician'),
]