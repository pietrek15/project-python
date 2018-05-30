from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list, name="list"),
    path('create/',views.article_create,name="create"),
    path('blog/view/<slug>/',views.article_detail,name="detail"),

]
