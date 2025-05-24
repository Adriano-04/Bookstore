import pytest

from product.models import Category

@pytest.mark.django_db

def test_category():
    category = Category.objects.create(
        title = "title test",
        slug = "slug test",
        description = "description test",
    )

    assert category.title == "title test"
    assert category.slug == "slug test"
    assert category.description == "description test"