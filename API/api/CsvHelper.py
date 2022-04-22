import pandas as pd
from collections import namedtuple
from .serizalizers import ResponseSerializer
import os.path

UserResponse = namedtuple('Response', ('characters', 'result'))
"""
    Create Csv class to get what we need to csv using pandas
"""
class CsvHelper:
    
    csv_folder = 'CSV'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    def __init__(self, result_dict, character_list):
        self.result_dict = result_dict
        self.character_list =  character_list
    
    """
        Function creating csv from information we got
        getting characters + compare result for them
        checking if csv already exist for them by compare id in db
        if exist returning his full file path otherwise creating him in folder CSV and return full file path
    """
    def create_csv(self):
        user_response = UserResponse(
        characters = self.character_list,
        result = self.result_dict
        )
    
        serializer = ResponseSerializer(user_response) 
        comp_id = serializer.data['result']['id']
        characters_info_df = pd.DataFrame.from_records(serializer.data['characters'])
        characters_info_df.loc[characters_info_df.index[0], 'Result'] = serializer.data['result']['result']
        characters_info_df['Result'] = characters_info_df['Result'].fillna('')
        print(characters_info_df)
        
        #create compare csv file by compare id in db
        csv_file_name = 'Compare_%d.csv' % (comp_id)
        
        file_location = os.path.join(self.csv_folder, csv_file_name)
        print(file_location)
        #check if file already exist to return to user his path
        if os.path.isfile(self.csv_folder + csv_file_name):
            print('Found ready csv')
        else:            
            characters_info_df.to_csv(file_location, index=False)
        final_file_path = os.path.abspath(os.path.abspath(file_location))
        return final_file_path

