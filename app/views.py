# Create your views here.

from django.http import HttpResponse
from app.models import News
from app.serializers import NewsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

from lxml import html
import requests


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def home(request):
    # news = News.objects.all()
    # serializer = NewsSerializer(news, many=True)
    # return JSONResponse(serializer.data)
    page = requests.get('http://www.bdnews24.com/')
    tree = html.fromstring(page.text)
    buyers = tree.xpath('//h3/text()')
    # prices = tree.xpath('//span[@class="item-price"]/text()')

    return HttpResponse(buyers)
