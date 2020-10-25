def ANDx(x,fx):
    """ANDS x and cofactor of x

    Args:
        x ([type]): [description]
        fx ([type]): [description]

    Returns:
        [type]: [description]
    """
    f = fx[0]
    nnv = len(f[0])
    nnc = len(f)
    i = abs(x) - 1 
    print("Here AND nc and f",nnc,f)
    if nnc <= abs(x) or i == 0:
        return f, nnv, nnc
    else:
        #nv = fx[1]
        #nc = fx[2]

        if x >= 0:
            mul = 1
        elif x <= 0:
            mul = 10

        print("Out of range",f,i)
        for cl in f:
            cl[i] = mul
            print("Out of range",f,i)
        nnv = len(f[0])
        nnc = len(f)
        return f, nnv,nnc 