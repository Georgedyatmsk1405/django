from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from app_houses.models import House

class LatestHouse(Feed):
    title="Объявления о продаже"
    link="/sitenews/"
    description="Самые свежие новости"

    def items(self) -> QuerySet:
        return House.objects.order_by('-published_at')[:5]

    def item_title(self, item:House) -> str:
        return item.description
    def item_link(self, item:House) -> str:
        return reverse('house-item', args=[item.pk])