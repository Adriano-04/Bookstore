import pytest
from product.models.product import Product

@pytest.mark.django_db
def test_product_create():
    product = Product.objects.create(
        title="Teste Produto",
        description="Teste descrição",
        price=10
    )

    assert product.title == 'Teste Produto'
    assert product.description == 'Teste descrição'
    assert product.price == 10
    assert product.id is not None
