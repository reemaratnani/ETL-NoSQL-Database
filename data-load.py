import os

import pandas as pd

import pymongo
import json


def import_content(filepath):

    client = pymongo.MongoClient('localhost', 27017)

    db = client['company_reviews'] 

    collection_name = 'reviews' 

    db_cm = db[collection_name]

    cdir = os.path.dirname(__file__)

    file_res = os.path.join(cdir, filepath)



    data = pd.read_csv('reviews.csv')

    data_json = json.loads(data.to_json(orient='records'))

    db_cm.remove()

    db_cm.insert(data_json)



if __name__ == "__main__":

  filepath = 'reviews.csv'  

  import_content(filepath)