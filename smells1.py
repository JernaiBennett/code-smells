def calculate_total_price(items):
    total = 0
    for item in items:
        if item == "apple":
            total += 1.0
        elif item == "banana":
            total += 0.5
        elif item == "cherry":
            total += 0.75
        elif item == "mango":
            total += 1.00
        elif item == "pineapple":
            total += 1.50
        elif item == "dragonfruit":
            total += 2.00
        elif item == "durian":
            total += 2.75
        else:
            print("Unknown item: " + item)
    if total >= 10:
        total *= 0.9
    return total


if __name__ == "__main__":
    print("run `pytest tests/smells1_test.py` instead.")
