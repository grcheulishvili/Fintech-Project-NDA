import json
import pickle

import numpy as np

__modeli = None
__svetebi = None

def load_data():
    global __modeli
    global __svetebi

    with open('server/data/svetebi.json','r') as f:
        __svetebi = json.load(f)['svetebi']
    with open('server/data/CRS_Model.pickle','rb') as file:
        __modeli = pickle.load(file)

def predict_price(transmission,fuel,previous_owner,year,km_driven):
    global __modeli
    global __svetebi

    if __svetebi == None:
        with open('server/data/svetebi.json','r') as f:
            __svetebi = json.load(f)['svetebi']
    if __modeli == None:
        with open('server/data/used_car_price_model.pickle','rb') as file:
            __modeli = pickle.load(file)

    x = []
    x[:8] = np.zeros(8,dtype='int32')
    x[5] = previous_owner
    x[6] = year
    x[7] = km_driven
    
    transmission_index = np.where(__svetebi==transmission)[0]
    fuel_index = np.where(__svetebi==fuel)[0]
    
    if transmission_index>=0:
        x[transmission_index] = 1
    if fuel_index>=2:
        x[fuel_index] = 1

    return '{:,}'.format(round(__modeli.predict([x])[0],2))
if __name__ == '__main__':
    load_data()