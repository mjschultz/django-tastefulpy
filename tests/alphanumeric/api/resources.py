from tastefulpy.authorization import Authorization
from tastefulpy.fields import CharField
from tastefulpy.resources import ModelResource
from alphanumeric.models import Product


class ProductResource(ModelResource):
    class Meta:
        resource_name = 'products'
        queryset = Product.objects.all()
        authorization = Authorization()
