from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
from .models import BlogArticle
from django import forms
from django.shortcuts import redirect, get_object_or_404

from .forms.auth_form import MyAuthForm
from .forms.create_blog_form import CustomCreateBlogForm

from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth import authenticate

from django.core.exceptions import ValidationError

# for custom login view
from django.contrib.auth import views as auth_views
from django.urls import reverse

'''
this is the view for home page. will display latest log entries
'''
def blogsite_home(request):

  articles = BlogArticle.get_latest_articles()

  prev_page = 0
  next_page = 2

  # let's just default to true
  has_next_page=True

  return render( request, 'blog/blog_home.html', {'articles': articles,  'prev_page':prev_page,  'next_page': next_page, 'has_next_page':has_next_page} )

'''
this is the general function top format the fetched blog article
'''
def __render_artricle(request, article):

  tags = article.tags.all()

  print ( tags )

  return render(request, 'blog/view_article.html', {'article': article , 'tags':tags})

def view_article_by_slug(request, seo_slug):

  #find the blog article that the seo_url points to
  # article = BlogArticle.objects.get(seo_url=seo_slug)
  article = get_object_or_404(BlogArticle, seo_url=seo_slug)

  return __render_artricle(request, article)

def view_article(request, id):

  article = get_object_or_404(BlogArticle, pk=id)
  # article = BlogArticle.objects.get(pk=id)

  return __render_artricle(request, article)

def __view_articles( **kwargs ):


  filters = {
    'publish_status':'PB'
  }

  if kwargs.get('tag', None ):
    filters['tags__url_slug'] = kwargs.get('tag')

  # limit to items per page
  articles_per_page = 3
  # dummy setting

  page = 1
  if kwargs.get('page', None) :
    page = kwargs.get('page')

  start = None
  stop = 3
  if page > 1 :
    start = (page-1)*articles_per_page
    stop += start  

  articles = BlogArticle.objects.filter( **filters ).order_by('publish_date').reverse()[ start : stop ]
  
  # for page data
  if page == 1:
    prev_page = 0  
  else:
    prev_page = page-1
  
  next_page = page+1

  has_next_page = False
  
  total_published = BlogArticle.get_total_published_articles( **kwargs  )
  
  if total_published > page*BlogArticle.articles_per_page :
    # no more next page
    has_next_page = True

  article_data = {
    'articles': articles, 
    'prev_page':prev_page,  
    'next_page': next_page, 
    'has_next_page':has_next_page
    }


  return article_data



def view_articles_by_tag(request, tag, page=1):

  kwargs = {
    'page' : page,
    'tag' : tag
  }

  article_data = __view_articles( **kwargs )



  return render( request, 'blog/blog_home.html', article_data )


def view_latest_articles(request, page=1):
  
  articles = BlogArticle.get_latest_articles(page)

  if page == 1:
    prev_page = 0  
  else:
    prev_page = page-1
  
  next_page = page+1
  total_published = BlogArticle.get_total_published_articles()
  if len(articles) == 0:
    # no more articles, invalid page
    return HttpResponseNotFound("no such page")         

  has_next_page = False
  if total_published > page*BlogArticle.articles_per_page :
    # no more next page
    has_next_page = True

  return render( request, 'blog/blog_home.html', {'articles': articles, 'prev_page':prev_page,  'next_page': next_page, 'has_next_page':has_next_page} )

def about_me(request):

  return render(request, 'about_me.html')



@login_required(login_url='login-page')
@permission_required('blogengine.add_BlogArticle', raise_exception=True)
def create_blog_article(request):

  print ( repr(request.user.is_authenticated) )

  if request.method == "POST" :
    
    form = CustomCreateBlogForm( request.POST, request.FILES )

    if form.is_valid() :
      form.save()
      return redirect("blog-home")
    else:
      print(repr(form.errors))
  else:
    form = CustomCreateBlogForm(  )

  return render(request, 'blog/create_blog_article.html', {'form':form})


def modify_blog(request, article_id):

  article = get_object_or_404(BlogArticle, pk=article_id)

  if request.method == "POST" :
    form = CustomCreateBlogForm( request.POST, request.FILES, instance=article )
    if form.is_valid() :
      form.save()

      return redirect("view_article", id=article_id)
  else:
    # load the blog aricle
    # or 404
    form = CustomCreateBlogForm( instance=article )



  return render(request, 'blog/create_blog_article.html', {'form':form})




# custom login view
class CustomLoginView(auth_views.LoginView):
  template_name = 'auth.html'

  # override to go to custom URL
  def get_success_url(self):
      url = self.get_redirect_url()
      if url:
          return url
      else:
        return reverse('blog-home')


# custom logout view
# since the default template is the registrations page
class CustomLogoutView(auth_views.LogoutView):
  template_name = 'logout_page.html'