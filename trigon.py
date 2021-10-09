
Тимур
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
      
    def is_triangle(self):
        if self.a <= 0 and self.b <= 0 and self.c <= 0:
            print("С отрицательными числами ничего не выйдет!")
        else:
            sides = sorted((self.a, self.b, self.c), key = lambda x : -x)
            if sides[0] < sides[1] + sides[2]:
                print("Ура, можно построить треугольник!")
            else:
                print("Жаль, но из этого треугольник не сделать.")

