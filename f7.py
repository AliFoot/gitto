# Defining the function with two parameters
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

# Calling the function
final_invoice = calculate_total(100, 0.20)
print(final_invoice)  # Outputs: 120.0
