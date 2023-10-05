from mathematics.number_theory.euclidean.euclidean import Euclidean

e = Euclidean()

print(e.solve_diophanthine(3, 4, 10))
print(e.solve_diophanthine(5, -7, 9))
print(e.solve_diophanthine(9, 23, 1))
print(e.solve_diophanthine(4, 6, 11))

print(e.solve_diophanthine(8, 2, 26))
print(e.solve_diophanthine(44, -17, 9))
print(e.solve_diophanthine(60, 9, 31))
print(e.solve_diophanthine(60, 9, 51))
