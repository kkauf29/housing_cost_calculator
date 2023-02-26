###
# Kim Kaufman
# Advanced Python Final
# 5/10/22
# Simple GUI that will change the label when the button is clicked. 


import tkinter as tk



def main():
    #sets up the main window
    root = tk.Tk()
    root.title("Click Me")
    root.geometry("500x500")
    root.configure(bg="green")
    
    

    
    #first label
    label = tk.Label(root, text="Nothing Happening")
    label.grid(column=0, row=0)
    
    def change_text():
        '''Changes label when button is clicked'''
        label = tk.Label(root, text="You have clicked a button")
        label.grid(column=0,row=0)
    
    button = tk.Button(root, text="Click Me", command=change_text)
    button.grid(column=0, row=1)
    
    
    root.mainloop()
    
main()     
 