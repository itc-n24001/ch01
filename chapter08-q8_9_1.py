from decimal import Decimal

diff_d = Decimal("10_000_000_000.2") - Decimal("10_000_000_000")
a = diff_d - Decimal("0.2")

print(a)


