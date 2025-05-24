import pytest

from product.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer():
    data = {
        "title" : "Serializer title",
        "description" : "Serializer description",
        "price" : 10,
    }

    serializer = ProductSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    product = serializer.save()

    assert product.title == data["title"]
    assert product.description == data["description"]
    assert product.price == data["price"]

    serializer = ProductSerializer(product)
    serializer_data = serializer.data

    assert serializer_data["title"] == data["title"]
    assert serializer_data["description"] == data["description"]
    assert serializer_data["price"] == data["price"]