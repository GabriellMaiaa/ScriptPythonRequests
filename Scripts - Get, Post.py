import requests
from requests.adapters import HTTPAdapter
import urllib3
import json

from urllib3 import Retry
session = requests.Session()
adapter = HTTPAdapter(max_retries=Retry(total=4, backoff_factor=1, allowed_methods=None, status_forcelist=[429, 500, 502, 503, 504]))
session.mount("http://", adapter)
session.mount("https://", adapter)


baseUrl ='https://compras.betha.cloud/compras-services'
headers = {'authorization':'Bearer 80a8059d-acf1-4d49-8e32-ec338d0d3f31'}
entidade = '1'
exercicio = '2011'
processo = '75'
idGerado = '648241'

def getConsulta (processo, exercicio):
    hasNext=True
    offset=0
    limit=100
    baseApi = f'{baseUrl}/api/processosadministrativo/{idGerado}/contratacao'
    
        # print(f"Buscando Processo {processo}")
    
    while(hasNext):                                        
        api=f"{baseApi}?filter=(numeroprocesso+in+('{processo}'))&limit={limit}&offset={offset}"
        
        response = session.get(api,headers=headers)
        result = response.json() if 'application/json' in response.headers.get('Content-Type') else json.loads(response.text)
            # print(result)
        hasNext = result['hasNext']
        offset = result['offset']+limit
            
        if ('content' in result ):
            if(result['content']):
                    #print(f"Encontrou resultado para o processo {processo} no ano {exercicio}")
                return result['content'][0]['id']
            else:
                    #print(f"Não Encontrou resultado para o processo {processo} no ano {exercicio}")
                return None