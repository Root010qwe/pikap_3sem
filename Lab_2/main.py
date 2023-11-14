from bub_oo.rectangle import Rectangle
from bub_oo.circle import Circle
from bub_oo.square import Square
def main():
    r = Rectangle(5, 5, "синего")
    c = Circle(5, "зеленого")
    s = Square( 5, "красного")
    print(r)
    print(c)
    print(s)
if __name__ == "__main__":
    main()