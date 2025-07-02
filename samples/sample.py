from pytemplate1.calculator import Calculator

calc = Calculator()

# 足し算
result = calc.add(1, 2)
print(f"1 + 2 = {result}")

# 引き算
result = calc.sub(3, 1)
print(f"3 - 1 = {result}")

# 掛け算
result = calc.mul(2, 3)
print(f"2 * 3 = {result}")

# 割り算
result = calc.div(6, 2)
print(f"6 / 2 = {result}")

try:
    result = calc.div(6, 0)
    print(f"6 / 0 = {result}")
except ValueError as e:
    print(f"Error: {e}")
