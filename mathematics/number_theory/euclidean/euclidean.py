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

        largerst_number = max(number1, number2)
        smallest_number = min(number1, number2)

        remainder = largerst_number % smallest_number

        if remainder == 0:
            return smallest_number

        while True:
            old_remainder = remainder

            largerst_number = smallest_number
            smallest_number = remainder

            remainder = largerst_number % smallest_number

            if remainder == 0:
                return old_remainder

    def gcd(self, *numbers) -> int:
        if len(numbers) < 2:
            raise ValueError("Cannot calculate gcd() of just one integer.")

        result = self._gcd(numbers[0], numbers[1])

        for i in range(2, len(numbers)):
            result = self._gcd(result, numbers[i])

        return result

    def _extended(self):
        pass

    def extended(self):
        pass
