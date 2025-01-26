from re import S
import numpy as np
def function(a, b, w,t):
    c = []
    for i in range(a):
        row = list(map(float, input(f'Enter values for row {i+1} separated by space: ').split()))
        c.append(row)
    matrix = np.array(c)
    
    print("Initial Matrix:")
    print(matrix)
    
    for j in range(b):
        sum_squares = 0
        for i in range(a):
            sum_squares += matrix[i][j] ** 2
        for i in range(a):
            matrix[i][j] = matrix[i][j] * w[j] / np.sqrt(sum_squares)
    
    print('Weighted Normalized Matrix:')
    print(matrix)
    vmin=[]
    vmax=[]
    for j in range(b):
        min_value = np.min(matrix[:,j])
        max_value = np.max(matrix[:,j])
        vmin.append(min_value)
        vmax.append(max_value)
    ideal_best = []
    ideal_worst = []
    for j in range(b):
      if(t[j]=='+'):
        ideal_best.append(vmax[j])
        ideal_worst.append(vmin[j])
      else:
        ideal_best.append(vmin[j])
        ideal_worst.append(vmax[j])
    Splus=[]
    Sminus=[]
    for i in range(a):
      S1=0
      S2=0
      for j in range(b):
        S1+=(matrix[i][j]-ideal_best[j])**2
        S2+=(matrix[i][j]-ideal_worst[j])**2
      Sminus.append(np.sqrt(S2))
      Splus.append(np.sqrt(S1))
    P=[]
    for i in range(a):
      P.append(Sminus[i]/(Splus[i]+Sminus[i]))
    ranks = np.argsort(P)[::-1] + 1

        


