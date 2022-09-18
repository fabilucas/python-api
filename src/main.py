import requests
import logger
import requestData
import transformData

def main():
    log = logger.Logger("main")
    req_data = requestData.RequestData()
    transform_data = transformData.TransformData()

    log.info("---------------------------------------------------------")
    log.info("------------------Lista Municipios por UF----------------")
    log.info("---------------------------------------------------------")
    

    result = req_data.get_requests(req_data.get_input_uf())

    #log.info(result)
    df = transform_data.create_dataframe(result)
    transform_data.generate_csv(df)

    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        log.info('Exit...')


if __name__ == '__main__':
	main()