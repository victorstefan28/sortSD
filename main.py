import random
import time
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
def sort_num(v):
    sort_numarare(v, max(v), max(v))
def radix_sort(v):
    nmax = max(v)
    p = 1
    _radix = 10
    while nmax // p > 0:
        sort_numarare(v, p, _radix)
        p *= _radix


def main():
    f = open("teste.in")
    T = f.readline()
    teste = []
    for line in f.readlines():
        n, valmx = line.split()
        n = int(n)
        valmx = int(valmx)
        teste.append((int(n), int(valmx)))
    print(teste)

    sortari = [radix_sort]
    for sortare in sortari:
        for test in teste:
            L = [random.randint(1, test[1]) for _ in range(test[0])]
            inc = time.time()
            #sort_numarare(L, len(L), 101)
            sortare(L)
            sf = time.time()
            print(f"{str(sortare.__name__)} a durat {round(sf-inc, 5)} secunde pentru {test[0]} valori in intervalul [1, {test[1]}]")




if __name__ == "__main__":
    main()