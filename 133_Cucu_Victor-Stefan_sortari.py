import random
import sys
import time
import math
def sort_numarare(v, n, mod): # pt radix
    fr = [0] * mod
    out = [0] * (len(v))

    for i in range(len(v)):
        fr[(v[i]//n)%mod] += 1
    for i in range(1,mod):
        fr[i] += fr[i-1]
    for i in range(len(v)-1, -1, -1):
        out[fr[(v[i]//n)%mod]-1] = v[i]
        fr[(v[i]//n)%mod] -= 1
    for i in range(len(v)):
        v[i] = out[i]


def insertion_sort(v):
    if len(v)>10**4:
        return "fail"
    for i in range(len(v)):
        x = v[i]
        j = i-1
        while j>=0 and x < v[j]:
            v[j+1] = v[j]
            j-=1
        v[j+1] = x


def sortat(v):
    for i in range(1,len(v)):
        if v[i-1] > v[i]:
            return "Nu"
    return "Da"

def merge_sort(v):
    if len(v) > 1:
        mj = len(v)//2
        st = v[:mj]
        dr = v[mj:]
        merge_sort(st);
        merge_sort(dr);
        # sortare prin interclasare ->
        i = 0
        j = 0
        k = 0
        while i < len(st) and j < len(dr):
            if st[i] < dr[j]:
                v[k] = st[i]
                i+=1
            else:
                v[k] = dr[j]
                j+=1
            k+=1
        #una din liste ramane cu elemente la final -> le adaugam
        while j<len(dr):
            v[k] = dr[j]
            j+=1
            k+=1
        while i<len(st):
            v[k] = st[i]
            i+=1
            k+=1

def partitie(v, st, dr):
    mj = (st + dr) // 2
    pivot = 0
    if v[mj] < v[st]:
        v[st], v[mj] = v[mj], v[st]
    if v[dr] < v[st]:
        v[st], v[dr] = v[dr], v[st]
    if v[mj] < v[dr]:
        v[mj], v[dr] = v[dr], v[mj]
    #mediana din 3
    pivot = v[dr]

    i = st-1


    for j in range(st,dr):
        if v[j]<=pivot:
            i+=1
            v[i],v[j]=v[j],v[i]
    v[i+1],v[dr]=v[dr],v[i+1]

    return i+1

def shell_sort(v):
    k = len(v)//2
    while k>0:
        for i in range(k,len(v)):
            temp = v[i]
            j = i
            while j>=k and v[j-k]>temp:
                v[j] = v[j-k]
                j-=k
            v[j] = temp
        k//=2
def q_sort(v, st, dr):
    if(st<dr):
        part_ind = partitie(v, st, dr)

        q_sort(v, st, part_ind-1)
        q_sort(v, part_ind+1, dr)
def q_sort_call(v):
    if sortat(v) == "Da":
        return
    if (max(v)-min(v)<=10):
        print("Q-sort nu poate sorta->recursion stack overflow") #
        return "fail"
    q_sort(v,0,len(v)-1)

def radix_sort(v):
    nmax = max(v)
    p = 1
    putere_doi = 1

    x = math.sqrt(nmax)
    while x>2:
        putere_doi+=1
        x//=2

    #alegem o baza favorabila-> observam ca pt numere mari bazele mici, 2^2,3,4,5 nu dau rezultate decente, nu vrem sa impartim nici de prea multe ori, nici de prea putine
    #daca alegem ca puterea lui 2 sa fie nr de factori 2 din radicalul maximului garantim minim o impartire(?)
    _radix = max(2**putere_doi, 8)
    while nmax // p > 0:
        sort_numarare(v, p, _radix)
        p = p << putere_doi


def main():
    f = open("teste.in")
    sys.setrecursionlimit(10**9)# pt q-sort
    T = int(f.readline())
    teste = []
    for line in f.readlines():
        n, valmx = line.split()
        n = int(n)
        valmx = int(valmx)
        teste.append((int(n), int(valmx)))
    print(teste)

    sortari = [radix_sort, merge_sort, q_sort_call, shell_sort, insertion_sort]
    for test in teste:
        init = [random.randint(0, test[1]) for _ in range(test[0])]
        for sortare in sortari:
            L = init.copy()
            inc = time.time()
            #for i in range(1000):
            rez = sortare(L)
            sf = time.time()
            if rez!="fail":
                print(f"{(str(sortare.__name__)).split('_sort')[0]}-sort a durat {round(sf-inc, 5)} secunde pentru {test[0]} valori in intervalul [{min(L)}, {max(L)}], {sortat(L)}")
            else:
                print(f"{(str(sortare.__name__)).split('_sort')[0]}-sort nu poate sorta")
        inc = time.time()
        init.sort()
        sf = time.time()
        print(f"Sortarea din python a durat {round(sf-inc, 5)} secunde pentru {test[0]} valori in intervalul [[{min(L)}, {max(L)}], {sortat(init)}")



if __name__ == "__main__":
    main()