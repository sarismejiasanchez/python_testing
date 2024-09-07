def calculate_total(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebook",
            "price": 100
        }
    ]

    assert calculate_total(products) == 100

def test_calculate_total_with_multiple_products():
    products = [
        {
            "name": "Book",
            "price": 20
        },
        {
            "name": "Pen",
            "price": 5
        }
    ]

    assert calculate_total(products) == 25


if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()

