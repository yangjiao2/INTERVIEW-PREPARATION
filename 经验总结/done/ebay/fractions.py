import math

def solution(fractions):
    # x/y+u/v -> x*v / y*v + u*y / y*v ->  (x*v + u*y) / y*v
    # 1. y and v are same, x + u -> xu; do xu % yv to make sure it can not reduce
    # 2. y and v are not same, transform to (x*v + u*y) / y*v; do (x*v + u*y) / y*v to make sure it can not reduce
    res = []
    for fraction in fractions:
        frac = fraction.split("+")
        frac1, frac2 = frac[0], frac[1]

        x, y = frac1.split("/")
        u, v = frac2.split("/")

        # fractions = [tuple(map(int, fraction.split('/'))) for fraction in fractions]


        intx, inty, intu, intv = int(x), int(y), int(u), int(v)

        if inty == intv:
            upper = intx+intu
            lower = inty

        else:
            upper = intx*intv + inty*intu
            lower = inty*intv

        # greatest common demonitor
        gcd = math.gcd(upper, lower)
        res.append( str(upper//gcd) + "/" + str(lower//gcd) )

    return res
