import re
import json

def parse_receipt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Extract all prices
    prices = re.findall(r'\b\d+\.\d{2}\b', content)
    prices = [float(price) for price in prices]

    # 2. Extract product names (word(s) before price)
    product_pattern = r'([A-Za-z ]+)\s+\d+\.\d{2}'
    products = re.findall(product_pattern, content)
    products = [product.strip() for product in products]

    # 3. Extract date
    date_match = re.search(r'\b\d{2}/\d{2}/\d{4}\b', content)
    date = date_match.group() if date_match else None

    # 4. Extract time
    time_match = re.search(r'\b\d{2}:\d{2}\b', content)
    time = time_match.group() if time_match else None

    # 5. Extract payment method
    payment_match = re.search(r'Payment Method:\s*(.+)', content)
    payment_method = payment_match.group(1) if payment_match else None

    # 6. Extract total
    total_match = re.search(r'Total:\s*(\d+\.\d{2})', content)
    total = float(total_match.group(1)) if total_match else sum(prices)

    # Create structured output
    parsed_data = {
        "date": date,
        "time": time,
        "products": products,
        "prices": prices,
        "total": total,
        "payment_method": payment_method
    }

    return parsed_data


if __name__ == "__main__":
    result = parse_receipt("raw.txt")
    print(json.dumps(result, indent=4))