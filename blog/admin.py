from django.contrib import admin
from blog.models import Post,Category
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin (SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    #fields = [ "title"]
    #exclude = ["birth_date"]
    list_display = ["title","author", "status",'published_date',"created_date"]
    list_filter =  ["status",'published_date',"author",]
    #ordering = ['-created_date']
    search_fields = ["title", "'content"]

    summernote_fields = ('content',)
 
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
