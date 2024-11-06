from rest_framework import serializers
from .models import Product, Order, OrderItem, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model."""
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'price', 'stock', 'image']

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the OrderItem model."""
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model with nested items."""
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'created_at', 'status', 'total_price', 'items']
        read_only_fields = ['user', 'created_at', 'total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total_price = 0

        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price * quantity
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total_price += price

        order.total_price = total_price
        order.save()
        return order
