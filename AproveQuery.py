import tkinter as tk
from tkinter import TclError,ttk,Tk
from services.configBase import ConfigBasicSql
from services.DataBaseTrataments import DatabaseImports

class AproveQuery:
    dti = DatabaseImports()
    cf =ConfigBasicSql()
    def ClearAll(self,text):
        self.dti.ClearDataAprove(self.cf.GetCon())
        text.delete('1.0',tk.END)
    def ReturnAllQuerys(self,text):
        text.insert(tk.END,self.dti.GetAllQuerys(self.cf.GetCon()))

    def CreateWindown(self):
        AproveW  =tk.Tk()
        AproveW.resizable(False,False)
        AproveW.title("Querys para aprovacao")

        Frame_01 = tk.Frame(AproveW)

        text = tk.Text(AproveW,height=10)
        text.grid(row=0,column=0,sticky=tk.EW)
        but_CopyAll = tk.Button(Frame_01,text="Copiar para Sql Query",command=lambda: self.ReturnAllQuerys(text))
        but_ClearAll = tk.Button(Frame_01,text="Apagar todos",command=lambda:self.ClearAll(text))

        Scroll = ttk.Scrollbar(AproveW,orient='vertical',command=text.yview)
        Scroll.grid(row=0,column=1,sticky=tk.NS)

        text['yscrollcommand'] = Scroll.set
        Frame_01.grid(column=0,row=1,pady=5)
        but_CopyAll.grid(column=0,row=0)
        but_ClearAll.grid(column=1,row=0,padx=5)

        AproveW.mainloop()
