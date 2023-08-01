import tkinter as tk
from tkinter import TclError,ttk,Tk
from services.configBase import ConfigBasicSql
from services.DataBaseTrataments import DatabaseImports

#SHOW PROCEDURE STATUS WHERE definer <> "mysql.sys@localhost" AND definer <>"mpopprt@127.0.0.1";

class ListProcedures:
    dti = DatabaseImports()
    cf =ConfigBasicSql()
    def ShowProcs(self):
        proceduresList  =tk.Tk()
        proceduresList.resizable(False,False)
        proceduresList.title("Procedures List")

        ProcList = self.dti.GetAllProcedures(self.cf.GetCon())
        ProcList = ProcList.strip(",")
        tree = ttk.Treeview(proceduresList,height=80,selectmode="extended")
        tree.insert('',tk.END,text=ProcList)

        tree.grid(row=0,column=0,sticky=tk.E)
        proceduresList.geometry("600x400")
        proceduresList.mainloop()