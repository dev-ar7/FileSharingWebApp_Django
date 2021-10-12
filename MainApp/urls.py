from django.conf.urls import url
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView,
                    search, about)
from . import views

app_name = 'MainApp'

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='MainApp-home'),
    url(r'^user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'^media/Files/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    url(r'^search/', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
]
