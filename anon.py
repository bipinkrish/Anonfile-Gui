from cgitb import text
from pathlib import Path
from tkinter import *
from tkinter import Place, filedialog, mainloop
from tkinter import Button, Label, ttk
import tkinter as tk
import webbrowser
from anonfile import AnonFile
from PIL import ImageTk, Image
anon=AnonFile()

class an: 

        def __init__(self) -> None:

                self.root = tk.Tk()

                self.frm = ttk.Frame(self.root).grid()
                self.root.title('ANONFILES GUI')
                self.root.geometry('800x400')
                #self.root.resizable(False, False)
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                x_cordinate = int((screen_width/2) - (800/2))
                y_cordinate = int((screen_height/2) - (400/2))
                self.root.geometry("{}x{}+{}+{}".format(800, 400, x_cordinate, y_cordinate))
                self.upload_filevar = tk.StringVar()
                self.download_var = tk.StringVar()
                self.backcheck = 0
       
                self.home()
                

        def callback(self,s):
                webbrowser.open_new_tab(s)

        def browseFiles(self):
                self.upload_filevar = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
                tk.Label(self.root, text=self.upload_filevar, font=('calibre', 10, 'bold')).place(x=400,y=150)

        def home(self):
                if self.backcheck:
                        try:
                                self.download_entry.destroy()
                                self.con_btn.destroy()
                                self.backbutton.destroy()
                                self.upload_filevar.set(text="")
                                self.root.update_idletasks()
                                
                        except:
                                pass   

                        try:
                                self.next_btn.destroy()
                                self.con_btn.destroy()
                                self.backbutton.destroy()
                                self.upload_label.destroy()
                                
                        except:
                                pass

                

                self.uploadbutton = Button(
                self.frm, text="Upload", command=self.upload, width=14, height=4)
                self.uploadbutton.place(x=250, y=150)
                self.downloadbutton = Button(
                self.frm, text="Download", command=self.download, width=14, height=4)
                self.downloadbutton.place(x=370, y=150)

        def download(self):
                self.uploadbutton.destroy()
                self.downloadbutton.destroy()
                self.download_entry = tk.Entry(self.root, textvariable=self.download_var, font=('calibre', 10, 'normal'), width=50)
                self.download_entry.place(x=220,y=150)
                self.con_btn = tk.Button(self.root, text='Confirm', command=self.confirmd, width=7, height=1)
                self.con_btn.place(x=350, y=220)
                self.backbutton = Button(self.frm, text="Back", command=self.back)
                self.backbutton.place(x=50, y=350)
                self.cons = tk.Label(self.root, text="                       WHEN YOU CLICK CONFIRM, PROGRESS HAPPENS IN BACKGROUND AND THE APPLICATION \n                    BECOMES UNRESPONSIVE JUST MINIMIZE IT WILL BECOME ACTIVE WHNE PROCESS IS FINISHED", font=('calibre', 10, 'bold')).place(x=1, y=50)
  

        def confirmd(self):
                d = self.download_entry.get()
                target_dir = Path.home().joinpath('Downloads')
                filename = anon.download(f"{d}", path=target_dir)
                print(filename)

        def upload(self):
                self.uploadbutton.destroy()
                self.downloadbutton.destroy()
                self.next_btn = tk.Button(self.root, text='select file', command=self.browseFiles, width=7, height=1)
                self.next_btn.place(x=250, y=150)
                self.con_btn = tk.Button(self.root, text='Confirm', command=self.confirm, width=7, height=1)
                self.con_btn.place(x=350, y=220)
                self.cons = tk.Label(self.root, text="                       WHEN YOU CLICK CONFIRM, PROGRESS HAPPENS IN BACKGROUND AND THE APPLICATION \n                    BECOMES UNRESPONSIVE JUST MINIMIZE IT WILL BECOME ACTIVE WHNE PROCESS IS FINISHED", font=('calibre', 10, 'bold')).place(x=1, y=50)
                self.backbutton = Button(self.frm, text="Back", command=self.back)
                self.backbutton.place(x=50, y=350)


        def confirm(self):
                 self.upload_filevar.replace("\/", "\\")
                 print(self.upload_filevar)
                 #os.system(f'cmd /c "curl -F "file=@{self.upload_filevar}" https://api.anonfiles.com/upload"')
                 upload = anon.upload(self.upload_filevar, progressbar=True)
                 self.upload_label = tk.Label(self.root, text=f"{upload.url.geturl()}", font=('calibre', 10, 'bold'), fg="blue", cursor="hand2" )
                 self.upload_label.place(x=250, y=290)
                 self.s=upload.url.geturl()
                
                 self.upload_label.bind("<Button-1>",lambda e: self.callback(self.s))

        def back(self):
                self.backcheck=1
                self.home()                
        

root=an()
root = mainloop()