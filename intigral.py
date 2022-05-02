from sympy import integrate, symbols, init_printing

x=symbols('x')
equ=((-1/15)*x**5)+((3/2)*x**4)-((37/3)*x**3)+(46*x**2)-((771/10)*x)+59

init_printing(use_unicode=True)

print(integrate(((-1/15)*x**5)+((3/2)*x**4)-((37/3)*x**3)+(46*x**2)-((771/10)*x)+59),(x,1,6))