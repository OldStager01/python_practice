print(0.1+0.1+0.1)
print(0.1+0.1+0.1 - 0.3) #wrong answer


from decimal import Decimal
result = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print(result)

from fractions import Fraction
result = Fraction(2,7)
print(float(result))