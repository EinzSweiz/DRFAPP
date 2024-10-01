from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello, unique_product_title
from .models import Product
from api.serializers import UserPublicSerializer
class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='products:detail', lookup_field='id')
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    owner = UserPublicSerializer(source='user', read_only=True)
    class Meta:
        model = Product
        fields = ['owner','url','edit_url', 'id', 'title', 'content', 'price', 'sale_price', 'discount']


    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'"{value}" is already product name')

    #     return value

    # def create(self, validated_data):
    #     obj = super().create(validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)


    def get_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None
    
    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("products:list_update", kwargs={'id': obj.id}, request=request)
        # return f'/api/products/{obj.id}/'