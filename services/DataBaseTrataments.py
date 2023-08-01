import mysql.connector
from services.configBase import ConfigBasicSql

class DatabaseImports:
    cf = ConfigBasicSql()
    def ReturnAllTables(self,params):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        cursor.execute("show tables")
        Result = str(cursor.fetchall())
        con.close()
        return Result
    
    def ReturnAllColumnsTables(self,params,Table):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME='"+Table+"'")
        Result = str(cursor.fetchall())
        con.close()
        return Result
    
    def ObterRegistros(self,params,Table,campo):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        cursor.execute("select COUNT("+campo+") FROM "+Table)
        Result = str(cursor.fetchall())
        con.close()
        return Result
    
    def ExecuteQuery(self,params,Query):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        try:
            cursor.execute(Query)
        except Exception as Ex:
            return "Sua query possui Erros: "+str(Ex)
        try:
            if (str(Query).find("DELETE")!=-1) or (str(Query).find("DROP")!=-1):
                    if(int(self.GetUser(params))!=1):
                        con.commit()
                        con.close()
                        return "Query executada com sucesso!!"
                    else:
                        return "Voce nao possui acesso para rodar esta Consulta, consulte o Gerenciador de banco de dados da sua organizacao."
            else:
               con.commit()
               con.close()
               return "Query executada com sucesso!!"     
            
                
        except Exception as ea:
            try:
                Result = str(cursor.fetchall())
                con.close()
                return Result    
            except Exception as e:
                return "Sua query possui erros de Sintaxe Erro: \n"+str(e)
            
    def GetUser(self,params):
         con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
         cursor = con.cursor()
         try:
            _usuario = str(self.cf.RerturnUserCurrent()).replace("\n","")
            cursor.execute("SELECT TipoUsuario FROM `AcessoBase` WHERE usuario='"+_usuario+"'")
            Result = str(cursor.fetchone())
            return Result.replace("(","").replace(")","").replace(",","")
         except:
            return "Obteve erro ao capturar Usuario"
    def EnviarQuery(self,params,Query):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        try:
            cursor.execute(Query)
            con.commit()
            con.close()
            return " \n Query  foi enviada com sucesso!"
        except Exception as Ex:
            return "\n Sua query possui Erros: "+str(Ex)
        
    def ClearDataAprove(self,params):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM `QueryDbaExecute`")
            con.commit()
            con.close()
            return " \n Query  foi enviada com sucesso!"
        except Exception as Ex:
            return "\n Sua query possui Erros: "+str(Ex)
        
    def GetAllQuerys(self,params):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        try:
            cursor.execute("SELECT QUERY,User FROM `QueryDbaExecute`")
            Result = str(cursor.fetchall())
            con.close()
            return Result
        except Exception as Ex:
            return "\n Sua query possui Erros: "+str(Ex)
        
    def GetAllProcedures(self,params):
        con = mysql.connector.connect( host =params[0],user =params[1],password = params[3],database = params[2])
        cursor = con.cursor()
        try:
            cursor.execute("SHOW PROCEDURE STATUS WHERE definer <> 'mysql.sys@localhost' AND definer <>'mpopprt@127.0.0.1';")
            Result = str(cursor.fetchall())
            con.close()
            return Result
        except Exception as Ex:
            return "\n Sua query possui Erros: "+str(Ex)

