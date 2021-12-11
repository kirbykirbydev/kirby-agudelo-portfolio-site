
from .views import blogsite_home,view_article, view_latest_articles,about_me,view_article_by_slug, create_blog_article,modify_blog, CustomLoginView, CustomLogoutView, view_articles_by_tag
from django.urls import path

urlpatterns = [

    path('', blogsite_home, name='blog-home'),
    path('article/<int:id>', view_article, name='view_article'),
    path('s/<slug:seo_slug>', view_article_by_slug, name='view_article_by_slug'),
    path('latest/<int:page>', view_latest_articles, name='latest-articles'),
    path('about-me', about_me, name='about-me'),

    path('create', create_blog_article),
    path('e/<int:article_id>', modify_blog),

    # built-in auth views
    path('auth-me', CustomLoginView.as_view(), name='login-page'),
    path('out-na-me', CustomLogoutView.as_view(), name='logout-page' ),

    # categories ( tags )
    path('category/<slug:tag>/<int:page>', view_articles_by_tag , name='articles-by-tag')
]