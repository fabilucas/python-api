import requests
import logger

class RequestData:

    def __init__(self):
        self.log =logger.Logger("request")      

    def get_input_uf(self):
        cd_uf = ""
        while(len(cd_uf) < 1):
            cd_uf = input('Digite o código da Unidade da Federação: ')

            if len(cd_uf) != 2:
                self.log.error('Quantidade de dígitos inválida!')
                cd_uf = ""
            else:
                return cd_uf


    def get_requests(self,cd_uf):
        request = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios'.format(cd_uf))
        municipios_por_uf = request.json()

        if 'erro' not in municipios_por_uf:
            self.log.info("Request Success!")
            return municipios_por_uf
        else:
            self.log.error('{}: Codigo da UF inválido.+'.format(cd_uf))


