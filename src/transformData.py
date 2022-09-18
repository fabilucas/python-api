import pandas as pd
import json
import csv
from pandas import json_normalize

class TransformData:

    def __init__(self) -> None:
        pass

    def create_dataframe(self, json_data): 
        dataset = pd.DataFrame(json_data)       
        df = json_normalize(json_data)
        print(df)
        return df
     
    def generate_csv(self, data):
        data.to_csv('teste.csv')
        
       
    
        
        


