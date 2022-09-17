import requests
import logger

def main():

    log = logger.Logger("main")

    log.info("---------LOCALIDADE IBGE--------")

    cep_input = input('Digite o CEP para a consulta: ')

    if len(cep_input) != 8:
        log.error('Quantidade de dígitos inválida!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        log.info("Request success!")
        log.info(address_data)
        
    else:
        log.error('{}: CEP inválido.'.format(cep_input))

    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        log.info('Exit...')

if __name__ == '__main__':
	main()