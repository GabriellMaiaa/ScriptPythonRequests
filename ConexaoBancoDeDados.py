dbConexao = "NOME DA CONEXÃO DO BANCO"# Script de conexão com o Banco de Dados
with #Botar a conexão do Banco as laConexao:  
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
                    #print(row.params)
                    # print(row.params)

                    idgerado = getId(row.params, row.params)    
                    # print(idgerado)    
                    if(idgerado != None):
                        print(idgerado)
                        print(row.hash_chave_dsk)
                        # Executar update no banco
                       

                #endFor
            #endWhile

    
        except Exception as e: 
            raise e
