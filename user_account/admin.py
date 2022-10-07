from django.contrib import admin  # noqa: F401

# Register your models here.
from .models import NewsletterSubscribers, UserProfile


class NewsletterSubscribersAdmin(admin.ModelAdmin):
    readonly_fields = ("subscription_date",)


# Register your models here.
admin.site.register(NewsletterSubscribers, NewsletterSubscribersAdmin)
admin.site.register(UserProfile)
