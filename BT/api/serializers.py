from BT.models import published_articles
from rest_framework.serializers import ModelSerializer


class MySerializers(ModelSerializer):
    class Meta:
       model = published_articles
       fields = '__all__'
