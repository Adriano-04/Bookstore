import pytest

from product.serializers import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    data = {
        "title" :  "title test",
        "slug" : "slug-test",
        "description" : "description test"
    }

    serializer = CategorySerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    category = serializer.save()

    assert category.title == data["title"]
    assert category.slug == data["slug"]
    assert category.description == data["description"]

    serializer = CategorySerializer(category)
    serializer_data = serializer.data

    assert serializer_data["title"] == data["title"]
    assert serializer_data["slug"] == data["slug"]
    assert serializer_data["description"] == data["description"]