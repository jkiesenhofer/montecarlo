from datetime import datetime
import os
import time
import numpy as np
import random
import array

def computeData(w,h,low,high):
    matrix = np.zeros((w,h))
    for i in range(len(matrix)):
        #q = np.sin(random())
        r=(random.randint(low,high))
        for j in range(len(matrix[i,:])):
            if r == j:
                matrix[i,j]=1.0
    dd = []
    for i in range(len(matrix)):
        a = ''
        for j in range(len(matrix[i,:])):
            if matrix[i,j] == 1:
                a = a+'+'
            else:
                a = a+' '
        dd.append(a)
    aa = []
    for p in range(h):
        b = ''
        for k in dd:
            b = b+k[p]
        aa.append(b)
    return aa
    
def computeChart(w,h,low,high,shift):
    t = shift
    chart = np.zeros((w,h))
    for i in range(len(chart)):
        #q = np.sin(random())
        r=(random.randint(low,high))
        for j in range(len(chart[i,:])):
            if j == int(h-(3.3*np.sin((i-t)/5)+10+4.3*np.sin((i-t)/20))):
                chart[i,j]=1.0
    dd = []
    for i in range(len(chart)):
        a = ''
        for j in range(len(chart[i,:])):
            if chart[i,j] == 1:
                a = a+'+'
            else:
                a = a+' '
        dd.append(a)
    aa = []
    for p in range(h):
        b = ''
        for k in dd:
            b = b+k[p]
        aa.append(b)
    return aa

def plotData():
    print('\n')
    for x in range(1):
        print(' ************ MONTE CARLO RANDOM NUMBER CHART ***********')
        print(' 300 -+------+------+------+------+------+------+------+- ')
        print('      |',aa[0],'|  ')
        print('      |',aa[1],'|  ')
        print(' 250 -+',aa[2],'+- ')
        print('      |',aa[3],'|  ')
        print('      |',aa[4],'|  ')
        print(' 200 -+',aa[5],'+- ')
        print('      |',aa[6],'|  ')
        print('      |',aa[7],'|  ')
        print(' 150 -+',aa[8],'+- ')
        print('      |',aa[9],'|  ')
        print('      |',aa[10],'|  ')
        print(' 100 -+',aa[11],'+- ')
        print('      |',aa[12],'|  ')
        print('      |',aa[13],'|  ')
        print('  50 -+',aa[14],'+- ')
        print('      |',aa[15],'|  ')
        print('      |',aa[16],'|  ')
        print('   0 -+------+------+------+------+------+------+------+- ')
        print('     1990   1995   2000   2005   2010   2015   2020   2025')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print('\n','                                         ', current_time)
    return
    
for x in range(14):
    aa = computeData(46,17,0,18)
    os.system('cls||clear')
    plotData()
    time.sleep(0.05)

for x in range(7):
    aa = computeData(46,17,3,6)
    os.system('cls||clear')
    plotData()
    time.sleep(0.05)
    
for x in range(14):
    aa = computeChart(46,17,3,6,x)
    os.system('cls||clear')
    plotData()
    time.sleep(0.1)
    
for x in range(14):
    aa = computeData(46,17,0,18)
    os.system('cls||clear')
    plotData()
    time.sleep(0.05)
    
for x in range(350):
    aa = computeChart(46,17,3,6,x)
    os.system('cls||clear')
    plotData()
    time.sleep(0.1)

#for a in range(17):
#    print(aa[a])

#print(aa)


#for x in range (0,13):
#    b = "Running " + "." * x + " " * x + "+" * 3*x
#    print (b)
#    time.sleep(0.1)
#
#for x in range (0,13):
#    b = "Running " + "." * x + " " * x + "+" * x
#    time.sleep(0.1)
#print('Hello, ' + os.getlogin() + '! How are you?')
