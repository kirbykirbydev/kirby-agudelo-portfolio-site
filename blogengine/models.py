from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
from datetime import datetime, timezone


# read variables from system environment


class PublishStatus(models.TextChoices):
  DRAFT = 'DR', 'Draft'
  PUBLISHED = 'PB', 'Publihsed'
  UNLISTED = 'UL', 'Unlisted'


class BlogTag(models.Model):
  name = models.CharField(max_length=64, unique=True, null=False, blank=False)
  url_slug = models.SlugField(max_length=64, unique=True, null=False, blank=False)
  description = models.TextField()

  def __str__(self):
      return self.name



class BlogArticle(models.Model):

  title = models.CharField(max_length=100)
  body = models.TextField()
  preview = models.TextField()
  created = models.DateTimeField(auto_now=False, auto_now_add=True)
  publish_date = models.DateTimeField(default=None)
  last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  publish_status = models.CharField( max_length=2, choices=PublishStatus.choices, default=PublishStatus.DRAFT)

  thumbnail_upload = models.ImageField(upload_to='blog_thumbs/',null=True, blank=True)

  seo_url = models.SlugField(max_length=100, unique=True, null=True, blank=True)

  tags = models.ManyToManyField(BlogTag)

  # ----
  articles_per_page = 3

  def save(self, *args, **kwargs):

    if not self.id:
      #process stuff that only occurs on create
      
      # if no seo URL indicated
      #if not self.seo_url:
      #  self.seo_url = slugify(self.title)
      pass
    super(BlogArticle, self).save(*args, **kwargs)

  @classmethod
  def get_latest_articles(cls, page=1):

    # dummy setting
    articles_per_page = 3

    start = None
    stop = 3
    if page > 1 :
      start = (page-1)*articles_per_page
      stop += start

    return cls.objects.all().filter(publish_status='PB').order_by('publish_date').reverse()[ start : stop ]

  @classmethod
  def get_total_published_articles(cls, **kwargs ):

    filters = {
      'publish_status':'PB'
    }

    if kwargs.get('tag',None):
      filters['tags__url_slug'] = kwargs.get('tag')

    # @todo this needs to be cached
    total_published = cls.objects.all().filter(**filters).count()    

    return total_published

  def format_published_days_ago(self):

    d = datetime.now(timezone.utc) - self.publish_date
    if d.days == 1:
      return "1 day ago"
    elif d.days == 0:
      return "today"
    else:
      return "%s days ago" % (d.days)