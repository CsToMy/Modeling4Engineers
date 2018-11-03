import numpy as np
import argparse
import sys
import matplotlib.pyplot as plt

parser=argparse.ArgumentParser(description='')
parser.add_argument('-g', '--graph', dest='graph', action='store', default=None)
parser.add_argument('-m', '--mtrail', dest='mtrail', action='store', default=None)
parser.add_argument('-c', '--mtrail_col', dest='m_col', action='store', type=int, default=None)
args=parser.parse_args()

if not args.graph:
    print >> sys.stderr, 'need graph'
    exit()

with open(args.graph) as ing:
    n=int(ing.readline().rstrip())
    A=[]
    for _ in range(n):
        A.append(map(int,ing.readline().rstrip().split()))
    B=[]
    for _ in range(n):
        B.append(map(int,ing.readline().rstrip().split()))
    m=len(B[0])
    P=[]
    for _ in range(n):
        P.append(map(float,ing.readline().rstrip().split()))

    
for i in range(n):
    for j in range(n):
        if A[i][j]==1:
            plt.plot([P[i][0],P[j][0]],[P[i][1],P[j][1]],'b')

if args.mtrail:
    with open(args.mtrail) as inm:
        neptuns=inm.readline().rstrip().split()
        M=[]
        for _ in range(m):
            M.append(map(int,inm.readline().rstrip().split()))
    lis=range(len(M[0]))
    if args.m_col or args.m_col==0:
        lis=[args.m_col]
    for i in lis:
        for j in range(len(M)):
            if M[j][i]==1:
                u=0
                v=0
                for k in range(n):
                    if B[k][j]==1:
                        u=k
                    elif B[k][j]==-1:
                        v=k
                plt.plot([P[u][0],P[v][0]],[P[u][1],P[v][1]],'r')

for i in range(n):
    plt.text(P[i][0],P[i][1],str(i), color='orange')

for j in range(len(B[0])):
    for i1 in range(n):
        for i2 in range(n):
            if B[i1][j]!=0 and B[i2][j]!=0 and i1!= i2:
                plt.text( float(P[i1][0]+P[i2][0])/2  ,  float(P[i1][1]+P[i2][1])/2, str(j), color='green'  )

plt.show()
