 
import tkinter as tk
import search

def printer (*args):
    
    ##Sorting the inputs for the FileSearch function
    inputs[1]=re_inputs[-1]
    inputs[0]=n_inputs[-1]
    i=2
    for element in test_lst:
        inputs[i]=element.get()
        i+=1
        
    ## Using the FilseSearch function
    col_lst,lst = search.FileSearch(inputs[0], inputs[1], inputs[4], inputs[5], inputs[3], float(inputs[2]))

    outputWindow(col_lst,lst)
    
def outputWindow(col_lst,lst):
    
    rot=tk.Tk() #Creates a window
    rot.columnconfigure(0,minsize=300, weight=3)
    total_rows=len(lst)
    total_columns=len(lst[0])
    
    ## Creating a grid for the output values
    for i in range(total_rows+1):
        for j in range(total_columns):
            rot.columnconfigure(j, weight=1)
            rot.rowconfigure(i,weight=1)
            if i==0: 
                if j==0:  ##The title column is wider to read the names properly
                    wid=20
                else:
                    wid=5
                e = tk.Entry(rot, width=wid, fg='black',
                               font=('Arial',12,'bold'))
                  
                e.grid(row=i, column=j, padx=1,pady=5, sticky='ew')
                e.insert(tk.END, col_lst[j]) #switching tk.END to 0 for test
            else:
                if j==0: #The first column with the name of the airfoils is wider
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
N_options=['5', '9']
    
    
root = tk.Tk() #Creates a window
re_inputs=[]
n_inputs=[]
test_lst=[]
inputs = ['','','','','','']
    
## Input for Reynolds Number used an Option Menu
row_re = tk.Frame(root) #Creates frame
row_re.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    
variable = tk.StringVar(root)
variable.set(Re_options[0])
    
re_dropdown = tk.OptionMenu(row_re,variable, *Re_options)
re_label = tk.Label(row_re, text='Choose a Reynolds Number: ')
re_label.pack(side=tk.LEFT)
re_dropdown.pack(side=tk.RIGHT)
    
Re_val=tk.StringVar(root)
Re_val.set("Re Value")
    

        
## Input for N value used an Option Menu
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

#i=2
## Input for text values used an Entry for inputs
for element in fields:
    row = tk.Frame(root)
    label = tk.Label(row,text=element, foreground ="black", background="white")
    ent = tk.Entry(row)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    label.pack(side=tk.LEFT)
    ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    test_lst.append(ent)
    #i+=1

## Creating buttons for searching and quitting    
button_search = tk.Button(root,text="Search", command = printer)
button_search.pack(side=tk.LEFT)
button_quit = tk.Button(root, text='Quit', command=root.destroy)
button_quit.pack(side=tk.LEFT, padx=5, pady=5)

def tracker(*args):
    
    ## Tracking the different values of Re and N
    Re_val.set(variable.get())
    N_val.set(variable2.get())
    re_inputs.append(Re_val.get())
    n_inputs.append(N_val.get())
    

variable.trace('w',tracker)
variable2.trace('w', tracker)


root.mainloop() #Keeps window Open


