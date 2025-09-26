import pytest
from sweetshop import Sweet, SweetShop

def test_add_and_restock_sweet():
    shop = SweetShop()
    laddu = Sweet("Laddu", 10.0, 5)
    shop.add_sweet(laddu)
    shop.restock_sweet("Laddu", 10)
    assert shop.inventory["Laddu"].quantity == 15

def test_sell_sweet_reduces_stock_and_returns_revenue():
    shop = SweetShop()
    barfi = Sweet("Barfi", 20.0, 10)
    shop.add_sweet(barfi)
    revenue = shop.sell_sweet("Barfi", 3)
    assert revenue == 60.0
    assert shop.inventory["Barfi"].quantity == 7

def test_sell_more_than_stock_raises_error():
    shop = SweetShop()
    jalebi = Sweet("Jalebi", 5.0, 2)
    shop.add_sweet(jalebi)
    with pytest.raises(ValueError):
        shop.sell_sweet("Jalebi", 5)
