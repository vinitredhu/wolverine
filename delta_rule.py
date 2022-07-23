import csv

with open('DATA.csv', 'r') as f:
    reader = csv.reader(f)
    t_e = list(reader)
print(t_e)

def output(t_e,w):
    for d in range(len(t_e)-1):
        val = 0
        for i in range(len(t_e[0])-1):
            val += w[i]*int(t_e[d+1][i])
        out[d] = val
    return out

dim = len(t_e[0])-1
w = [0.0]*(len(t_e[0])-1)
out = [0.0]*(len(t_e)-1)
n = 0.01



iter = int(input("enter no of iterations you want"))
for p in range(iter):
    dw = [0.0]*(len(t_e[0])-1)
    out = output(t_e,w)
    print(out)
    for d in range(len(t_e)-1):
        for i in range(len(t_e[0])-1):
            dw[i] += 0.01*(int(t_e[d+1][dim])-out[d])*int(t_e[d+1][i])
    for i in range(len(dw)):
        w[i]+=dw[i]
    print(w)
input("bye")