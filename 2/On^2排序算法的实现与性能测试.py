 -*- coding: utf-8 -*-
from random import randint
import timeit

def bubbleSort(alist):
    exchange=False
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                exchange=True
        if not exchange:
            break
    return alist

def selectionSort(alist): ### 找到未排序部分的最小值，将其与未排序部分的最小索引位置(i)的值交换
    for i in range(len(alist)): ### 外层循环：未排序列表的计数器所在位置（minposition 此位置还未经排序）  
        minposition=i
        for j in range(i,len(alist)): ### 寻找最小值 ： 小于 最小索引，则交换；
            if alist[minposition]>alist[j]:### 逐个将未排序部分所有元素 与 最小索引位置的元素 比较: 遍历；
                minposition=j  ### 下一个(j)元素，继续与最小元素比较；直到，找到最小元素
        alist[i],alist[minposition]=alist[minposition],alist[i] ### 内循环之外  ###  将最小值  与 最小索引位置元素  交换
    return alist

def insertionSort(alist):### a. 将  正排序位置元素（当前值）  与 已排序元素逐个比较，放到合适的位置  
    for i in range(1,len(alist)):### b.  alist[:i-1]为已排序部分  ,假设alist[0]为有序，i从1 开始   
        currentvalue=alist[i] ### c. 外层循环 指向  当前值（正排序的元素 alist[i]）
        position=i
        while alist[position-1]>currentvalue and position>0:###d.  将当前值 逐个  与 前面的值（已排序） 比较
            alist[position]=alist[position-1] ### e. 如果 当前值 小于 已排序部分的这个位置的值，则将 这个值 向后 挪一位（第一次，不会覆盖当前值）
            position=position-1  ### f. 将 与当前值作比较的值的位置   更新  更小 索引位置 
        alist[position]=currentvalue ### g 要么 当前值 大于 这个值，要么position<1，循环结束 ### h. 将当前值放到  合适的位置
    return alist

def shellSort(alist):
    gap=len(alist)//2
    while gap>0:
        for startpos in range(gap):
            gapInsertionSort(alist,startpos,gap)
        gap=gap//2
    return alist

def gapInsertionSort(alist,startpos,gap):
    #希尔排序的辅助函数
    for i in range(startpos+gap,len(alist),gap):
        position=i
        currentvalue=alist[i]
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap
        alist[position]=currentvalue

max=5000
list=[randint(-max,max) for x in range(max)]
#使用切片可以真正将一份list复制给其他变量，如果不用切片，即alist=list，只是指针而已。
alist=list[:]
blist=list[:]
clist=list[:]
dlist=list[:]

'''
运行次数(number)只能设置成1，因为内存中alist、blist等指向同一个对象，该对象第一次排序后就已经是有序列表了。
所以在这种情况下会发生有趣的现象。按照短路冒泡排序的性质，它在碰到一个有序列表以后会立刻停止遍历，所以不管它的number是1还是10，time都几乎没变化
但其他排序方法，就算对有序列表进行排序，交换是不需要了，但是还要遍历&比较，所以他们的运行次数变多的话，time依旧变大
之前我就是把number设置成100，发现短路冒泡排序简直太快了，才发现这个问题。
'''
t1=timeit.Timer('bubbleSort(alist)','from __main__ import bubbleSort,alist')
print('短路冒泡排序: %s s' %t1.timeit(number=1))

t2=timeit.Timer('selectionSort(blist)','from __main__ import selectionSort,blist')
print('选择排序: %s s' %t2.timeit(number=1))

t3=timeit.Timer('insertionSort(clist)','from __main__ import insertionSort,clist')
print('插入排序: %s s' %t3.timeit(number=1))

t4=timeit.Timer('shellSort(dlist)','from __main__ import shellSort,dlist')
print('希尔排序: %s s' %t4.timeit(number=1))



