# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:43:51 2021

@author: ADMIN
"""

import tkinter as tk 
import os
import json
i= tk.Tk()
i.title('SPEND')
i.geometry('500x300')
i.configure(bg='#95CACA')
#f=open('spend.txt','a')
mylabel = tk.Label(i, text='記帳本')
mylabel.pack()
mylabel2 = tk.Label(i, text='請輸入物品及金額')
mylabel2.pack()
mylabel3 = tk.Label(i, text='物品',width=5)
mylabel3.pack()
e = tk.Entry(i,bd=4)
e.pack()
mylabel3 = tk.Label(i, text='金額')
mylabel3.pack()
h = tk.Entry(i)
h.pack()
m= tk.Label(i, text='目前所花金額')
m.pack()
## Create a dictionary to store string-value pair
all_items = {}
## Read json file and make it a dict
t = tk.Text(i,width=20, height=5)
c = tk.Text(i,bg='#95CACA',width=10, height=5)

k=0
Counts = 0
try:
    with open('spend.json',"r+") as f:
        try:
            all_items = json.loads(f.read())            
            for key in all_items:
                t.insert('insert',key)
                t.insert('insert','.')
                t.insert('insert',all_items[key][0])
                t.insert('insert','-')
                t.insert('insert',all_items[key][1])
                t.insert(tk.INSERT,'\n')
                k= k + all_items[key][1]
                Counts = int(key)+1
        except :
            pass
except OSError:
    print('No file found')
    
def insert_point():
    global Counts
    global k
    #print(type(Counts))
    var = e.get()
    var2 = h.get()
    t.insert('insert',Counts)
    t.insert('insert','.')
    t.insert('insert', var)
    t.insert('insert', '-')
    t.insert('insert', var2)
    t.insert(tk.INSERT, '\n')
    e.delete(0,len(var))
    h.delete(0,len(var2))
    #all_items[var] = int(var2)
    all_items[str(Counts)] = [var,int(var2)]
    Counts = Counts + 1
    z = k + int(var2)
    k=z
    c.delete("1.0", tk.END)
    c.insert('insert',z)
    
def delete_point():    
    mkey = de.get()
    de.delete(0,len(mkey))
    try:
        global k
        global Counts
        k = k - all_items[mkey][1]
        del all_items[mkey] 
        t.delete("1.0", tk.END)
        c.delete("1.0", tk.END)
        c.insert('insert',k)
        for key in all_items:
                t.insert('insert',key)
                t.insert('insert','.')
                t.insert('insert',all_items[key][0])
                t.insert('insert','-')
                t.insert('insert',all_items[key][1])
                t.insert(tk.INSERT,'\n')
                Counts = int(key) + 1
    except:
        pass
    
    
c.delete("1.0", tk.END)
c.insert('insert',k)
c.pack()


b1 = tk.Button(i, text='輸入', width=10,
               height=2, command=insert_point)
b1.pack()

d= tk.Label(i, text='刪除物品')
d.pack()
de = tk.Entry(i)
de.pack()

b2 =tk.Button(i,text='刪除',width=10,height=2,command=delete_point)
b2.pack()

t.pack()
i.mainloop()

## Store dictionary into json files
with open('spend.json','w') as f:
    json.dump(all_items,f)
#f.close()





