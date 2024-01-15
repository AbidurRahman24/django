from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam
router.register('', views.ArticleViewSet) # ekta entena toiri korlam

urlpatterns = [
    path('', include(router.urls)),
    # path('articles/<int:article_id>/', SpecificArticleView.as_view(), name='specific_article'),
]