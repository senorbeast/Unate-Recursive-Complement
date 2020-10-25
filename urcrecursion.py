import numpy as np
import pandas as pd

def getF(filen):
    """ Func info stored as tuple
        Where 0th element - Func in PCN form (cubelist) SOP
        1st element - number of variables
        2nd element - number of cubes
        3rd element - Tautology or not, 1st element (3rd row) in file format is number of non-dont care
        So if 0 then all elements in that cube are DC so cubelist is tautology

    Args:
        filen ([str]): [description :filename of file in pcn format]

    Returns:
        [Tuple]: [description :tuple of bollfunc(PCN), no. of var ,no. of cubes]
    """
    f = open(filen, "r")
    llist = []
    for line in f:
        stripped_line = line.strip()
        lnlist = (stripped_line).split()
        map_object = map(int, lnlist)   #convert string to numbers or it applies int() to a list of elements
        lnlist = list(map_object)   
        llist.append(lnlist)
    # llist = [int((line.strip())).split() for line in f]
    f.close()
    #print(llist)
    nvar = llist[0][0]
    ncube = llist[1][0]
    #print(nvar,ncube,len(llist))
    slist = llist[2:2+ncube]
    nnlist = []
    #taut = 0
    for fe in slist:#removing 1st element number of non dont care var
        #if fe[0] == 0:
            #taut = 1
        fe = fe[1:fe[0]+1]
        nnlist.append(fe)
    #print(nnlist)
    func = [[11 for x in range(nvar)] for y in range(ncube)]
    for r in range(ncube):
        for c in range(len(nnlist[r])):
            if nnlist[r][c] >= 0:
                plr = nnlist[r][c]
                func[r][plr-1] = 1
            if nnlist[r][c] <= 0:
                plr = abs(nnlist[r][c])
                func[r][plr-1] = 10

    return func,nvar,ncube

#print(getF(fname))
ex = ([[11, 11, 1,1,11],[11,10,1,1,11],[11,10,1,1,11],[11,10,1,1,11]],5,4)
#print(ex[0])
def simpComp(func):
    """Finds Complement of simple function in PCN format
        Cases i) F = dont care cube
              ii) F = empty cube
              iii) F = single cube 
    Args:
        func ([Tuple]): [description :Tuple of Func, no. of vars ,no. of cubes]

    Returns:
        [Tuple]: [description :same as f]
    """
    fl = func[0]
    nvar = len(fl[0])  
    ncube = len(fl)
    #tnv = len(func[0])
    #tnc = len(func)
    # if tnc == 0:
    #     print('Fuckedup')
    dc = [11 for x in range(nvar)]
    ec = [00 for x in range(nvar)]
    ecc = []
    print("Almost Done")
   
    if (dc in fl) or ():                # fl[0] ==dc should also work i think bcoz in base conditon of recursion only 1 cube list is present,but we have redunduncy so idk
        empty = ([[]],nvar,0)
        return empty

    if (ec in fl) or (ecc in fl) or (ncube == 0):              # fl[0] ==ec should also work i think
        deli = (dc, nvar, 1)
        return deli
    
    else:
        ndc = 0
        z = [1, 10]
        ndc = 0
        truev = []
        falsev = []
        for j in range(nvar):
            p = fl[0]
            if p[j] in z:
                ndc+=1
            if p[j] == 1:
                truev.append(j)
            if p[j] == 10:
                falsev.append(j)
            
        print("NDC",ndc)
        #print("T",truev)
        #print("F",falsev)
        dc2 = [[11 for x in range(nvar)] for y in range(ndc)]
        print("DC2",dc2)
        l = 0
        for k in range(nvar):
            #print(k,nvar)
            if k in truev:
                dc2[l][k] = 10
                l += 1
            if k in falsev:
                dc2[l][k] = 1
                l += 1
        print("aftersimcomp",dc2)
        nnv = len(dc2[0]) 
        nnc = len(dc2)
        return dc2,nnv,nnc

#ex2 = simpcomp(ex)

def writeFile(func,fname):
    """Writes Func info stored in tuple to .pcn file format

    Args:
        func ([Tuple]): [description :FuncPCN, nvar, ncubes]
        fname ([str]): [descripion :filename of file, just for name of output file]
    """
    f= open( "op"+fname,"w+")
    fl = func[0]
    nv = len(fl[0])
    nc = len(fl)
    f.write(str(nv))
    f.write('\n')
    f.write(str(nc))
    f.write('\n')
    for i in fl:
        z = [1, 10]
        ndc = 0
        for j in i:
            if j in z:
                ndc+=1
        if nc == 0:
            f.write(str(''))
        else:
            f.write(str(ndc))
        for j in range(len(i)):
            if i[j] == 1:
                s = " " + str(j+1)
                f.write(s)
            if i[j] == 10:
                b = -1*(j+1)
                s1 = " " + str(b)
                f.write(s1)
        
        f.write('\n')
    f.close()

#writefile(ex2,fname)

def binateTest(func):
    """Gives most binate var, as specified in pdf...Too much

    Args:
        func ([Tuple]): [description :FuncPCN, nvar, ncubes]

    Returns:
        [int]: [description : binate var no. were variables starts from x1, x2 .....]
    """
    fl = func[0]
    nv = func[1]
    #nc = len(fl[0])
    print(".", end=" ")
    # nc = func[2]
    # taut = func[3]
    btest = 0
    cols = []
    for i in range(1,nv+1):
        a = "x"+str(i)
        cols.append(a)
    #print(cols)
    df = pd.DataFrame(fl, columns = cols)  
    z = np.zeros((5,nv), dtype=int)
    tc = pd.DataFrame(z, columns = cols, index = ['T', 'C', 'Sum', 'Sub','B'])
    #tc.at['T', 'x1'] = 1
    for column in df.columns:
        cn = str(column)  #colname
        tc.at['T', cn] = (df[column] == 1).sum()
        tc.at['C', cn] = (df[column] == 10).sum()
        tc.at['Sum', cn] = tc.at['T', cn] + tc.at['C', cn]
        tc.at['Sub', cn] = abs(tc.at['T', cn] - tc.at['C', cn])
        if ((tc.at['T', cn]) * (tc.at['C', cn]) !=  0):
            tc.at['B', cn] = 1
        elif ((tc.at['T', cn]) + (tc.at['C', cn]) == 0):
            tc.at['B', cn] = -1

    binv = tc.loc[['B']].values.flatten()
    ####################GOT THE TABLE######################

    maxbin = np.amax(binv)
    if maxbin == 1: 
        binate = (np.argwhere(binv == np.amax(binv))).flatten()
        sumvl = []
        subvl = []
        for i in binate:
            sumv = tc.loc['Sum']['x'+str(i+1)]
            sumvl.append(sumv)
            subv = tc.loc['Sub']['x'+str(i+1)]
            subvl.append(subv)
            #print(i)

        mostcv = (np.argwhere(sumvl == np.amax(sumvl))).flatten()
        allminsub = (np.argwhere(subvl == np.amin(subvl))).flatten()
        mostcvi = []
        allminsubi = []
        #print(mostcv,"test")
        #print(allminsub,"test2")
        
        for i in mostcv:
            a = binate[i]
            mostcvi.append(a)
        for i in allminsub:
            a = binate[i]
            allminsubi.append(a)
        #print(allminsubi,"Test3")
        frst = False
        #print(binate,"Binate")
        #print(tc)
        #print("newmost",mostcvi,allminsubi)
        
        if len(mostcvi) == 1:
            btest = mostcvi[0]
        else :
            for i in mostcvi:
                if (i in allminsubi) and frst == False :
                    btest =i
                    frst = True
    elif maxbin == 0:
        unate = (np.argwhere(binv == 0)).flatten()
        sumuvl = []
        for i in unate:
            sumuv = tc.loc['Sum']['x'+str(i+1)]
            sumuvl.append(sumuv)
        #print(sumuvl, unate)
        idx = np.argmax(sumuvl)
        btest = unate[idx]

    mbivar = btest + 1
    #print(mbivar,"Selected Var")
    #print(tc)
    #print(fl)
    return mbivar

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
    
    #nv = fx[1]
    #nc = fx[2]

    if x >= 0:
         mul = 1
    elif x <= 0:
        mul = 10

    #print("Out of range",f,i)
    for cl in f:
        try:
            cl[i] = mul
        except IndexError:
            pass
        
     #print("Out of range",f,i)
    nnv = len(f[0])
    nnc = len(f)
    return f, nnv,nnc 
       

def ORx(fx,fxx):
    f1 = fx[0]
    f2 = fxx[0]
    #nv = fx[1]
    #nc = fx[2]
    fn = f1 + f2
    nnv = len(fn[0])
    nnc = len(fn)
    return fn,nnv,nnc

def coFtr(x,func):
    #nv = func[1]
    f = func[0]
    nc = len(f)
    
    to_del = []
    if x >=0:
        pos = x -1 
        
        for cl in range(nc):
            if f[cl][pos] == 10:
                to_del.append(cl)
            if f[cl][pos] == 1:
                f[cl][pos] = 11
            if f[cl][pos] == 11:
                pass
    if x <=0:
        pos = abs(x) -1 
        for cl in range(nc):
            if f[cl][pos] == 1:
                to_del.append(cl)
            if f[cl][pos] == 10:
                f[cl][pos] = 11
            if f[cl][pos] == 11:
                pass
    fn= []
    for i in range(nc):
        if i not in to_del:
            fn.append(f[i])

    nnv = len(fn[0])
    nnc = len(fn)
    return fn,nnv,nnc 

#print(binateTest(ex))


foo, fif, fel, fbelse= 0, 0, 0, 0
print(foo,fif,fel)
def Complementr(ff):
    global foo 
    global fif 
    global fel
    global fbelse
    #if ff is simple find complement directly
    foo +=1
    nvar = ff[1]
    ncube = ff[2]
    cl = ff[0]
    print('CLout',cl)
    dc = [11 for x in range(nvar)]
    ec = [00 for x in range(nvar)]
    ee = [[]]
    ee1 = []
    print("foo-",foo)
    #bf = 0
    #nc = len(ff[0][0])
    if (dc in cl) or (ec in cl) or (len(cl) in [0,1]) or (ee in cl) or (ee1 in cl) or (ncube ==0):
        fif +=1
        print("BEFORE comp",ff)
        comp = simpComp(ff)
        print("fif -",fif)
        print("comp",comp)
        return comp
    else:
        fel+=1
        #do recursion
        fbelse +=1
        bx = binateTest(ff)
        print('BEforeelse',fbelse,ff,"Binate Var",bx)
        P = Complementr(coFtr(bx, ff))
        print("PP",P,bx)
        print("fel-",fel)
        N = Complementr(coFtr(-bx,ff))
        print("NN",N, bx)
        P = ANDx(bx,P)
        N = ANDx(-bx,N)
        print('CLelse',cl)
        print("GG")
        print("OR",ORx(P, N))
        return (ORx(P, N))

filename = "part2.pcn"
writeFile(Complementr(getF(filename)),filename)