
def is_triangle(sides):
    a, b, c = sides
    return (a != 0 and b != 0 and c != 0) and (a + b > c and b + c > a and c + a > b)
    
def equilateral(sides):
    """ a, b e c sao iguais"""
    a, b, c = sides    
    return is_triangle(sides) and a == b == c

def isosceles(sides):
    """Dois lados iguais, apenas um diferente e maior"""
    a, b, c = sides
    return is_triangle(sides) and ((a == b and a > c) or (a == c and a > b) or (b == c and b > a)) or (a == b == c)


def scalene(sides):
    """Todos os lados diferentes"""
    a, b, c = sides    
    return is_triangle(sides) and (a != b and b != c and c != a)