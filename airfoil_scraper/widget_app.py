# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:13:48 2021

@author: frank
"""
import tkinter as tk
import search

def printer (*args):
    inputs[1]=re_inputs[-1]
    inputs[0]=n_inputs[-1]
    #print('final RE: ', re_inputs[-1])
    #print('final N: ', n_inputs[-1])
    i=2
    for element in test_lst:
        #print(element.get())
        inputs[i]=element.get()
        i+=1
    #print('\n', str(inputs))
    col_lst,lst = search.FileSearch(inputs[0], inputs[1], inputs[4], inputs[5], inputs[3], float(inputs[2]))
    #print(col_lst)
    #print(lst)
    outputWindow(col_lst,lst)
    
def outputWindow(col_lst,lst):
    rot=tk.Tk()
    #rot.geometry()
    rot.columnconfigure(0,minsize=300, weight=3)
    #rot.rowconfigure(weight=3)
    total_rows=len(lst)
    total_columns=len(lst[0])
    # code for creating table
    for i in range(total_rows+1):
        for j in range(total_columns):
            rot.columnconfigure(j, weight=1)
            rot.rowconfigure(i,weight=1)
            if i==0:
                if j==0:
                    wid=20
                else:
                    wid=5
                e = tk.Entry(rot, width=wid, fg='black',
                               font=('Arial',12,'bold'))
                  
                e.grid(row=i, column=j, padx=1,pady=5, sticky='ew')
                e.insert(tk.END, col_lst[j]) #switching tk.END to 0 for test
            else:
                if j==0:
                    wid=20
                else:
                    wid=5
                e = tk.Entry(rot, width=wid, fg='black',
                               font=('Arial',12,'bold'))
                  
                e.grid(row=i, column=j, padx=1,pady=5, sticky='ew')
                e.insert(tk.END, lst[i-1][j])
    root.mainloop()
    
fields = ['Enter the desired CL/CD ratio: ',
              'Enter the desired tolerance for the CL/CD ratio: [leave black for default tolerance of 5%]: ',
              'Enter the max camber percentage [leave blank to not filter]: ',
              'Enter the max thickness percentage [leave blank to not filter]: ']
Re_options = ['50K', '100K', '200K', '500K', '1000K']
N_options=['N5', 'N9']
    
    
root = tk.Tk()
re_inputs=[]
n_inputs=[]
test_lst=[]
inputs = ['','','','','','']
    
# Input for Reynolds Number
row_re = tk.Frame(root)
row_re.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    
variable = tk.StringVar(root)
variable.set(Re_options[0])
    
re_dropdown = tk.OptionMenu(row_re,variable, *Re_options)
re_label = tk.Label(row_re, text='Choose a Reynolds Number: ')
re_label.pack(side=tk.LEFT)
re_dropdown.pack(side=tk.RIGHT)
    
Re_val=tk.StringVar(root)
Re_val.set("Re Value")
    

        
 # Input for N value
row_n = tk.Frame(root)
row_n.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    
variable2 = tk.StringVar(root)
variable2.set(N_options[0])
    
n_dropdown = tk.OptionMenu(row_n,variable2, *N_options)
n_label = tk.Label(row_n, text='Choose an N value: ')
n_label.pack(side=tk.LEFT)
n_dropdown.pack(side=tk.RIGHT)
    
N_val=tk.StringVar(root)
N_val.set("N Value")
    

str_out=tk.StringVar(root)
str_out.set("Output")

i=2
#Input for text values
for element in fields:
    row = tk.Frame(root)
    greetings = tk.Label(row,text=element, foreground ="black", background="white")
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    greetings.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    test_lst.append(ent)
    #i+=1
    
button_search = tk.Button(root,text="Search", command = printer)
button_search.pack(side=tk.LEFT)
button_quit = tk.Button(root, text='Quit', command=root.quit)
button_quit.pack(side=tk.LEFT, padx=5, pady=5)

def my_show(*args):
    Re_val.set(variable.get())
    N_val.set(variable2.get())
    re_inputs.append(Re_val.get())
    n_inputs.append(N_val.get())
    #print('Reynolds: ',Re_val.get())
    #print('N: ', N_val.get())

variable.trace('w',my_show)
variable2.trace('w', my_show)


root.mainloop()
