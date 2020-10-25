def ORx(fx,fxx):
    f1 = fx[0]
    f2 = fxx[0]
    
    #nv = fx[1]
    #nc = fx[2]
    fn = f1 + f2
    nnv = len(fn[0])
    nnc = len(fn)
    return fn,nnv,nnc

fx = ([[11, 11, 11, 11, 11]], 5, 1)
fxx = ([[]], 5, 1)

print(ORx(fx,fxx))