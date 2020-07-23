def count_change(denomination_quantities):
    total = 0
    # TODO put code here
    for d in denomination_quantities:
        q = denomination_quantities[d]
        subtotal = q * d
        total += subtotal

    return total


denomination_quantities = {
    1: 0,
    5: 1,
    10: 1,
    25: 3,
}


def currency(amount):
    return f"${amount:.2f}"


a = count_change(denomination_quantities) / 100
print(currency(a))
# Expected result: 93
# Try changing the quantities and adding other denominations

# SOLUTION
# for d in denomination_quantities:
#     q = denomination_quantities[d]
#     subtotal = q * d
#     total += subtotal
