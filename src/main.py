import requests
import logger

def main():

    log = logger.Logger("main")

    log.info("---------LISTA MUNICIPIOS POR UF--------")

    cd_uf = input('Digite o código da Unidade da Federação: ')

    if len(cd_uf) != 2:
        log.error('Quantidade de dígitos inválida!')
        exit()

    request = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/{}/municipios'.format(cd_uf))

    municipios_por_uf = request.json()

    if 'erro' not in municipios_por_uf:
        log.info("Request success!")
        log.info(municipios_por_uf)
        
    else:
        log.error('{}: Codigo da UF inválido.'.format(cd_uf))

    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        log.info('Exit...')

if __name__ == '__main__':
	main()