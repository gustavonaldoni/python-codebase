from pprint import pprint


class Euclidean:
    """
    A class containing the algorithms for number theory described
    by Euclides in he'x book "Elements".
    """

    def _gcd(self, number1: int, number2: int) -> int:
        if not isinstance(number1, int) or not isinstance(number2, int):
            raise TypeError(f"Cannot calculate gcd() of non integers.")

        if number1 == number2 and number2 == 0:
            raise ValueError("Cannot calculate gcd(0,0).")

        largest_number = max(number1, number2)
        smallest_number = min(number1, number2)

        remainder = largest_number % smallest_number

        if remainder == 0:
            return smallest_number

        while True:
            old_remainder = remainder

            largest_number = smallest_number
            smallest_number = remainder

            remainder = largest_number % smallest_number

            if remainder == 0:
                return old_remainder

    def gcd(self, *numbers: int) -> int:
        if len(numbers) < 2:
            raise ValueError("Cannot calculate gcd() of just one integer.")

        result = self._gcd(numbers[0], numbers[1])

        for i in range(2, len(numbers)):
            result = self._gcd(result, numbers[i])

        return result

    def _gcd_steps(self, number1: int, number2: int) -> int:
        """
        Calculates the steps involved on the Euclidean Algorithm
        of gcd(number1, number2). Returns a list of tuples of the form
        (largest_number, quotient, smallest_number, remainder).
        """
        if not isinstance(number1, int) or not isinstance(number2, int):
            raise TypeError(f"Cannot calculate gcd() of non integers.")

        if number1 == number2 and number2 == 0:
            raise ValueError("Cannot calculate gcd(0,0).")

        result = []

        # largest_number = quotient * smallest_number + remainder

        largest_number = max(number1, number2)
        smallest_number = min(number1, number2)

        quotient = largest_number // smallest_number
        remainder = largest_number % smallest_number

        result.append((largest_number, quotient, smallest_number, remainder))

        if remainder == 0:
            return result

        while True:
            old_remainder = remainder

            largest_number = smallest_number
            smallest_number = remainder

            quotient = largest_number // smallest_number
            remainder = largest_number % smallest_number

            result.append((largest_number, quotient, smallest_number, remainder))

            if remainder == 0:
                return result

    def _extended(self, a: int, b: int) -> tuple:
        old_a, old_b = (a, b)
        a, b = (abs(a), abs(b))

        old_r, r = (a, b)
        old_x, x = (1, 0)
        old_y, y = (0, 1)

        while r != 0:
            quotient = old_r // r

            (old_r, r) = (r, old_r - quotient * r)
            (old_x, x) = (x, old_x - quotient * x)
            (old_y, y) = (y, old_y - quotient * y)

        if old_a < 0:
            old_x *= -1

        if old_b < 0:
            old_y *= -1

        return (old_x, old_y)

    def extended(self, *coefficients: int):
        pass

    def solve_diophanthine(self, a: int, b: int, c: int) -> tuple:
        """
        Calculates the result of the Diophantine Equation
        ax + by = gcd(a, b), where a, b and c are integers. Returns
        a tuple of the form (x, y).
        """
        gcd = self.gcd(a, b)
        gcd_divides_c = c % gcd == 0

        if not gcd_divides_c:
            return False
        
        a, b, c = (a // gcd, b // gcd, c // gcd)

        return tuple([c * number for number in self._extended(a, b)])
