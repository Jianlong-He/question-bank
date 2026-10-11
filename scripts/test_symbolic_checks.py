"""Verify the limited exact checker rejects false identities and non-linear roots."""
import unittest
from fractions import Fraction
from symbolic_checks import polynomial, solve_linear


class PolynomialChecks(unittest.TestCase):
    def test_factorization(self):
        self.assertEqual(polynomial('x**2+13*x+36'), polynomial('(x+4)*(x+9)'))
        self.assertNotEqual(polynomial('x**2+13*x+36'), polynomial('(x+3)*(x+12)'))

    def test_fractional_coefficients_and_multiple_variables(self):
        self.assertEqual(polynomial('0.1*x+2*x/5'), polynomial('x/2'))
        self.assertEqual(polynomial('3*r*t+8-8'), polynomial('3*t*r'))

    def test_roots_and_absolute_constant(self):
        self.assertEqual(solve_linear('7*x-5','3*x+39','x'), Fraction(11))
        self.assertEqual(solve_linear('-x+abs(-23)','-48','x'), Fraction(71))
        self.assertEqual(solve_linear('3*x','2','x'), Fraction(2,3))

    def test_unsupported_or_nonunique_equations_are_rejected(self):
        for left,right in [('x**2','9'),('x','x'),('x+1','x'),('x+y','2')]:
            with self.assertRaises(AssertionError):solve_linear(left,right,'x')
        for expression in ['1/x','abs(x)','x**(-1)']:
            with self.assertRaises(AssertionError):polynomial(expression)


if __name__=='__main__':unittest.main()
