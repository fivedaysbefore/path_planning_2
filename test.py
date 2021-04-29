global a,b,c
a = 1
b = 2
c = 3
def test_here():
    global a,b,c
    b = a
    b += a
    a += c
    c +=4
    print(a,b,c)
test_here()
test_here()