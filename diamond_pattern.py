#diamond pattern
c =eval(input('maximum columns in the pattern : '))
for i in range(c+1):
    print(" "*(c-i)+" *"*i)
for i in range(c-1,0,-1):
     print(" "*(c-i)+" *"*i)
