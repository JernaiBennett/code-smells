def calculate_total_price(items):
    """Calculate the total price of items with a discount for orders >= DISCOUNT_THRESHOLD."""
    total = sum(ITEM_PRICES.get(item, 0) for item in items)
    
    if total >= DISCOUNT_THRESHOLD:
        total *= (1 - DISCOUNT_RATE)
    
    return total


# Constants
ITEM_PRICES = {
    "apple": 1.0,
    "banana": 0.5,
    "cherry": 0.75,
    "mango": 1.00,
    "pineapple": 1.50,
    "dragonfruit": 2.00,
    "durian": 2.75
}

DISCOUNT_THRESHOLD = 10.0
DISCOUNT_RATE = 0.1


if __name__ == "__main__":
    print("run `pytest tests/smells1_test.py` instead.")