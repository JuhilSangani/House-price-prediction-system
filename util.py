import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_predicted_price(location, sqft, bath, bhk):
    try:
        index_location = __data_columns.index(location.lower())
    except:
        index_location = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if index_location >= 0:
        x[index_location] = 1

    return round(__model.predict([x])[0], 2)

def get_location():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    with open("columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("house_price_prediction_system.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("..done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location())
    # print(get_predicted_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_predicted_price('1st Phase JP Nagar', 1000, 3, 3))
    # print(get_predicted_price('Indira Nagar', 1000, 2, 2))
    # print(get_predicted_price('Indira Nagar', 1000, 3, 3))
