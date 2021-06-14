# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:16:09 2021

@author: ADMIN
"""

import tkinter as tk
c=tk.Tk()
c.geometry('500x800+100+300')
c.title("first")
c.configure(bg='#95CACA')
lb=tk.Label(c,text='HI，請選擇要執行的事件',width=20,font=50,pady=10,fg='black',bg='#95CACA',compound='center')
lb.pack()
but=tk.Button(c,text='記帳')
but.pack()
but2=tk.Button(c,text='查詢已有物品')
but2.pack()



c.mainloop()
