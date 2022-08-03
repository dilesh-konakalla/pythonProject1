class KLU1:
    def areaRectangle(a, b):
        return (a * b)

    def perimeterRectangle(a, b):
        return (2 * (a + b))

    a = float(input('enter a:'))
    b = float(input('enter b:'))

    print("Area = ", areaRectangle(a, b))
    print("Perimeter = ", perimeterRectangle(a, b))

    def areaCircle(r):
        return (3.14*r*r)

    def perimeterCircle(r):
        return (2*3.14*r)

    r = float(input('enter r:'))

    print("Area = ", areaCircle(r))
    print("Perimeter = ", perimeterCircle(r))

    def areaTriangle(q, w, e):
        return ( 0.5*q*e)

    def perimeterTriangle(q, w, e):
        return (q+w+e)

    q = float(input('enter q:'))
    w = float(input('enter w:'))
    e = float(input('enter e:'))

    print("Area = ", areaTriangle(q, w, e))
    print("Perimeter = ", perimeterTriangle(q, w, e))