import numpy as np

def doc_scrap():
    with open('../data/doc.txt', 'r') as file:
        f = file.readlines()
        odd_lin = []

        l = int(np.floor(len(f)/2))
        for n in range(l):
            odd_lin.append(f[2*n+1])
        return odd_lin



