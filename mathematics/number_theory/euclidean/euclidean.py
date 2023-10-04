from pprint import pprint


class Euclidean:
    """
    A class containing the algorithms for number theory described
    by Euclides in he's book "Elements".
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

    def _extended(self, a: int, b: int, c: int) -> tuple | bool:
        """
        Calculates the result of the Diophantine Equation
        ax + by = c, where a, b and c are integers. Returns
        a tuple of the form (x, y) or False if gcd(a, b) does
        not divide c.
        """

        a_copy = a
        b_copy = b

        a = abs(a)
        b = abs(b)

        gcd = self.gcd(a, b)
        gcd_divides_c = c % gcd == 0

        if not gcd_divides_c:
            return False

        a = a // gcd
        b = b // gcd
        c = c // gcd

        x = "x"
        y = "y"

        largest_number = max(a, b)
        smallest_number = min(a, b)

        table = list()

        gcd_steps = self._gcd_steps(a, b)
        pprint(gcd_steps)

        gcd_steps = gcd_steps[2:]

        table.append([(largest_number, x, 1), (largest_number, y, 0)])
        table.append([(smallest_number, x, 0), (smallest_number, y, 1)])

        i = 0

        for largest_number, quotient, smallest_number, remainder in gcd_steps:
            first_row = table[i]
            second_row = table[i + 1]

            new_x = first_row[0][2] - second_row[0][2]
            new_y = first_row[1][2] - second_row[1][2]

            table.append([(largest_number, x, new_x), (largest_number, y, new_y)])

            i += 1

        last_x = table[-2][0][2] - table[-1][0][2]
        last_y = table[-2][1][2] - table[-1][1][2]
        
        table.append([(1, x, last_x), (1, y, last_y)])

        result_x = last_x * c
        result_y = last_y * c

        pprint(table)

        if a_copy < 0:
            result_x = -result_x

        if b_copy < 0:
            result_y = -result_y

        return (result_x, result_y)

    def extended(self, *coefficients: int):
        pass
