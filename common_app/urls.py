from django.urls import path, include

from common_app import views

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', views.ViewAllArticles.as_view(), name='home'),
    path('create_article/', views.CreateArticleView.as_view(), name='create article'),
    path('view_article/<int:pk>/', views.ArticleDetailView.as_view(), name='view article'),
    path('edit_article/<int:pk>/', views.ArticleUpdateView.as_view(), name='edit article'),
    path('delete_article/<int:pk>/', views.ArticleDeleteView.as_view(), name='delete article'),
    path('view_all_user_articles/<int:pk>/', views.ArticlesUserAllView.as_view(), name='all user articles'),
    path('create_comment/<int:pk>/', views.NewCommentView.as_view(), name='create comment'),
    path('edit_comment/<int:pk>/<int:article_pk>/', views.CommentUpdateView.as_view(), name='edit comment'),
    path('delete_comment/<int:pk>/<int:article_pk>/', views.CommentDeleteView.as_view(), name='delete comment'),


]
