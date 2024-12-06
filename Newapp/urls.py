
from django.contrib import admin
from django.urls import path
from Newapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('streak/', views.streak, name='streak'),
    path('affirmation/', views.affirmation, name='affirmation'),
    path('articles/', views.articles, name='articles'),
    path('reviews/', views.reviews, name='reviews'),
    path('article1/', views.article1, name='article1'),
    path('article2/', views.article2, name='article2'),
    path('article3/', views.article3, name='article3'),
    path('article4/', views.article4, name='article4'),
    path('article5/', views.article5, name='article5'),
    path('article6/', views.article6, name='article6'),
    path('support/', views.support, name='support'),
    path('emergency/', views.emergency, name='emergency'),
    path('addreview/', views.addreview, name='addreview'),
    path('extrareviews/', views.extrareviews, name='extrareviews'),
    path('imagedelete/<int:id>', views.imagedelete),
]
