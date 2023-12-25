from rest_framework.decorators import api_view
from rest_framework.response import Response
from BT.models import published_articles
from  . serializers import MySerializers

@api_view(['GET'])
def getarticles(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getArticles(request):
    articles = published_articles.objects.all()
    serializer = MySerializers(articles,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getArticles(request,pk):
    article = published_articles.objects.get(id = pk)
    serializer = MySerializers(article,many = False)
    return Response(serializer.data)