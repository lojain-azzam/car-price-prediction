# Contents of pre_processing_sample.py file


import pandas as pd
import pickle
from datetime import datetime, timedelta


def load_pickle(path: str) -> pickle:

    with open(path, 'rb') as pkl_file:
        return pickle.load(pkl_file)

# Load necessary pickles
encoder = load_pickle('research/pkls/onehot_encoder.pkl')
scaler = load_pickle('research/pkls/min_max_scaler.pkl')
model = load_pickle('research/pkls/gradient_model.pkl')

# List of features name need onehot encoding
one_hot_features = ['name', 'color', "glass_type", "fuel_type", "car_type", 
                    "license_type", "lime_type"]

# Dictionary of possible words of ex owner value
ex_owner_dict = {
    'zero': ['0', '٠', 'صفر', 'صفرض', 'صفرر', 'لا شيء ','Zero','O'],
    'ones' : ['1', 'أولى', 'اولى', 'اولا', 'واحد', 'اول', 'ياولى', 'اوله', 'انا','اولي', 'واله', 'ولا', 'واحدة', 'أولئ', 'ولى',
            'أولي', 'اولئ', 'اولة', 'اةلي', '١', 'ا'],
    'two' : ['2', 'تانيه', 'ثني', 'تاني', 'ثاتيه', 'تانية', 'ثاني', 'ثانبه', 'تانبه', 'ثانيا',
            'يانيه', 'ثانية', 'ثانيه', 'اثنان', '٢'],
    'three' : ['3', 'ثالثة', 'ثالثه', 'تالثه', 'تالته', 'ثالث', 'التالته', '٣'],
    'four'  : ['4', 'اربعه', 'رابعه', 'اربعة', 'رابعة','٤'],
    'five'  : ['5', 'خامسة', 'خامسه', 'خامساً', 'خمسة', 'خمسه', '٥']
}




### Calculate the number of passengers from equation
def get_passengers_number(passengers:str) -> int:


    sum_digit:int = 0

    for char in passengers:
        if char.isdigit():
            int_char = int(char)
            sum_digit = sum_digit + int_char
    
    return sum_digit



### Takes the user value of ex owner and find whether the
### value contains in ex_owner_dict, will return the number if it exisit.

def get_ex_owner_number(ex_owner:str) -> int:

    for item in ex_owner.split(' '):
        for ex_owner_id in ex_owner_dict.keys():
            if item in ex_owner_dict.get(ex_owner_id):
                return int(ex_owner_dict.get(ex_owner_id)[0])
    return 0



def get_speedometer_number(car_speedometer:str) -> int:
    for item in car_speedometer.split(' '): 
        if item.isdigit():
            if len(item) <= 3:
                item = int(item) * 1000
            return int(item)
    return 0



### Extracts the company name from the given name.
def get_company_name(name:str) -> str:

    company = name.split(' ')[0]
    return company


def encoding(sample:list) -> list:

    to_onehot = pd.DataFrame(sample, columns=one_hot_features)
    
    sample_encoded = encoder.transform(to_onehot)
    return list(sample_encoded.values[0])




def min_max_scaler(sample:list) -> list:

    sample_scaled = scaler.transform(sample)
    return sample_scaled




    """
    Predicts the price of the given sample using a trained model.
    """

def pridict_price(sample:list) -> float:

    sample = pd.DataFrame([sample])
    price = model.predict(sample)
    return price



