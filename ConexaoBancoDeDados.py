dbConexao = "NOME DA CONEXÃO DO BANCO"# Script de conexão com o Banco de Dados
with SybaseConnect().connect_from_odbc(dbConexao) as laConexao:  
        cursor = laConexao.cursor()
        
        laSQL=""--Consulta que percorre
        try:
            number_of_rows = cursor.execute(laSQL)
            print(laSQL)

            while True:
                records = cursor.fetchmany(50)
                if not records:
                    break
                #endIf
                
                for row in records:
                    #print(row) 
                    #print(row.i_chave_dsk2)
                    # print(row.i_chave_dsk3)

                    idgerado = getId(row.i_chave_dsk3, row.i_chave_dsk2)    
                    # print(idgerado)    
                    if(idgerado != None):
                        print(idgerado)
                        print(row.hash_chave_dsk)
                        # Executar update no banco
                        updateId( laConexao,idgerado,row.hash_chave_dsk )

                #endFor
            #endWhile

    
        except Exception as e: 
            raise e
