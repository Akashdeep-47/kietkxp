from django.urls import path
from . views import PostTemplateView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('', PostTemplateView.as_view(), name='blog-home'),
    path('search/',views.search,name='search'),
    #path('category/<str:category>',PostCategoryView.as_view(),name='post-category'),
    path('books/',views.books,name='post-books'),
    path('lab_accessories/',views.labs,name='post-lab'),
    path('electronics/',views.electronics,name='post-electronics'),
    path('others/',views.others,name='post-others'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
]





