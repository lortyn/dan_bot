from fractions import Fraction


def fract(text: str):
    try:
        numerator, denominator = map(int, text.strip().split('/'))
        fraction = Fraction(numerator, denominator)
        simplified_fraction = fraction.limit_denominator()
        return f"Сокращенная дробь: {simplified_fraction.numerator}/{simplified_fraction.denominator}"
    except Exception as e:
        return 'Ошибка ввода'


