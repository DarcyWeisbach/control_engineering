#!/usr/bin/env python3
from control import matlab
import control
import matplotlib.pyplot as plt
import numpy as np


def bode_diagram():
    a=[]
    b=[]
    print("分子の最高次は？")
    bunshi = int(input("入力："))
    print("分子の高次の項の係数を入れてください")
    for i in range(bunshi+1):
        print("s^",(bunshi-i),"の係数を入力してください",sep='')
        a.append(float(input("入力：")))
    print('\n')    
    print("分母の最高次は？")
    bunbo = int(input("入力："))
    print("分母の高次の項の係数を入れてください")
    for i in range(bunbo+1):
        print("s^",(bunbo-i),"の係数を入力してください",sep='')
        b.append(float(input("入力：")))
    print('\n')  

    Ga=matlab.tf(a,b)
    print(Ga)
    fig=plt.figure()
    matlab.bode(Ga)
    plt.show()
    fig.savefig("ボード線図.jpg")
    fig = plt.figure()
    matlab.nyquist(Ga)
    plt.show()
    fig.savefig("ナエキスト線図")

def oresen():
    print("第13回の配布資料のボード線図の基本形にわけてください\n何個基本形はありますか")
    n=int(input())
    x=np.arange(0.001,100.0,0.01)
    x1=np.arange(0.001,100.0,0.01)
    q1=np.array([0.001,0.01,1,10,100])
    q=np.ones((n,4))
    w=np.ones((n,4))
    y=np.ones((n,10000))
    fig=plt.figure()
    ax=plt.subplot()
    ax.set_xscale('log')
    for i in range(n):
        print(i+1,"個目の基本形はどれですか．以下の番号を入れてください．\n0：G(s)=K,     1：G(s)=s,     2：G(s)=1/s,\n3：Ts+1,      4：G(s)=1/(Ts+1)")
        kihonkei=int(input("入力："))
        if kihonkei==0:
            print("Kの値は？")
            k=float(input("入力："))
            q[i] = np.array([0.001, 0.01, 1, 10, 100])

            y[i]=np.ones(10000)
            y[i]=20*np.log10(np.abs(k))*y[i]
            w[i]=np.log10(w[i])
            #y[i]=(np.abs(k))*y[i]

        if kihonkei==1:
            q[i] = np.array([0.001, 0.01, 1, 10, 100])
            y[i]=20*np.log10(x)
            w[i]=90*np.log10(w[i]*10)

        if kihonkei==2:
            q [i]= np.array([0.001, 0.01,10, 100])
            y[i]=-20*np.log10(x)
            w[i]-90*np.log10(w[i]*10)

        if kihonkei ==3:
            print("Tの値は？")
            T=float(input("入力："))
            num=np.count_nonzero(x < 1/T)
            num02=np.count_nonzero(x<0.2/T)
            num5=np.count_nonzero(x<5/T)
            a=np.zeros(num)
            a1=20*np.log10(x[num:10000])-20*np.log10(1/T)
            q[i] = np.array([0.01, 0.2/T, 5/T, 100])
            iso02=np.zeros(2)
            iso=45*np.log10(10)
            iso5=90*np.log10(10*np.ones(2))
            y[i]=np.hstack((a,a1))
            w[i]=np.hstack((iso02,iso5))
            print("1/T：",1/T)
            print("0.2/T",0.2/T)
            print("5/T",5/T)
        
        if kihonkei==4:
            print("Tの値は？")
            T=float(input())
            num=np.count_nonzero(x<=1/T)
            num=np.count_nonzero(x < 1/T)
            num02=np.count_nonzero(x<0.2/T)
            num5=np.count_nonzero(x<5/T)
            a=np.log10(np.ones(num))
            #a1=-20*np.log10(x[num:1000]-1/T)
            a1=-20*np.log10(x[num:10000])+20*np.log10(1/T)
            q[i] = np.array([0.01, 0.2/T, 5/T, 100])
            iso02=np.zeros(2)
            iso5=-90*np.log10(10*np.ones(2))
            y[i]=np.hstack((a,a1))
            w[i]=np.hstack((iso02,iso5))
            print("1/T：",1/T)
            print("0.2/T",0.2/T)
            print("5/T",5/T)
    for i in range(n):
        ax.plot(x,y[i])
    z=np.zeros(10000)
    for i in range(n):
        z+=y[i]
    ax.plot(x,z,color='red')
    print('赤色が回答です')
    plt.show()
    fig.savefig("ボード線図手書き.jpg")
    fig = plt.figure()
    ax = plt.subplot()
    ax.set_xscale('log')
    for i in range(n):
        ax.plot(q[i],w[i])
    z=np.zeros(4)
    #for i in range(n):
    #    z+=w[i]
    #ax.plot(q1,z,color='red')
    plt.show()
    fig.savefig("位相図.jpg")
    print("合成するのがめんどくさいので後は気を付けて合成してください.\n例えば重なり合ってるとわからないためボード線図（曲線）と比較してください．")

def hurwitz():
  
    print("分母の最高次は？")
    saikouzi=int(input("入力："))
    a=np.ones(saikouzi+1)
    delta=np.ones(saikouzi)
    for i in range(saikouzi+1):
        print(saikouzi-i,"次の係数は？")
        a[saikouzi-i]=float(input("入力："))
    for i in range(saikouzi):
        if i==0:
            delta[i]=a[saikouzi-1]
        if i==1:
            if saikouzi==2:
                 matrix=[[a[saikouzi-1],0],[a[saikouzi],a[saikouzi-2]]]
            else:
                matrix=[[a[saikouzi-1],a[saikouzi-3]],[a[saikouzi],a[saikouzi-2]]]
            delta[i]=np.linalg.det(matrix)
        if i==2:
            if saikouzi==3:
                matrix=[[a[saikouzi-1],a[saikouzi-3],0],[a[saikouzi],a[saikouzi-2],0],[0,a[saikouzi-1],a[saikouzi-3]]]
            if saikouzi==4:
                matrix=[[a[saikouzi-1],a[saikouzi-3],0],[a[saikouzi],a[saikouzi-2],a[saikouzi-4]],[0,a[saikouzi-1],a[saikouzi-3]]]
            delta[i]=np.linalg.det(matrix)
        if i==3:
            matrix=matrix=[[a[saikouzi-1],a[saikouzi-3],0,0],[a[saikouzi],a[saikouzi-2],a[saikouzi-4],0],[0,a[saikouzi-1],a[saikouzi-3],0],[0,a[saikouzi],a[saikouzi-2],a[saikouzi-4]]]
            delta[i]=np.linalg.det(matrix)
    print("左から順にΔ1 , Δ2 , Δ3 , ...",delta)
    

        

    
while 1:
    print("行いたい処理を以下から選んでください")
    print("0：終了     1：ボード線図を描く     2：ボード線図を折れ線で書く     3：フルビッツの方法（４次まで）")
    select=int(input())
    if select==0:
        exit(0)
    if select==1:
        print("分子と分母について以下に従って入力してください．分解する必要はないですが,分子と分母はそれぞれ展開してください．")
        bode_diagram()
        print("\n")
    if select==2:
        print("分子と分母について以下に従って入力してください．分解して基本形が複数掛け算されている状態にしてください")
        oresen()
        print("\n")
        
    if select==3:
        print("4次までにしてください．例外処理してないため，5次以降は計算がおかしくなります．")
        hurwitz()
        print("\n")
    else:
        pass



            
