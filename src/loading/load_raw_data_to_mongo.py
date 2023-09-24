from database.mongo import Mongo

import pandas as pd

import glob
import os
import re


def data_to_mongo():
    path_files = os.path.join("./data/raw", "*.csv")
    file_list = glob.glob(path_files)

    for file in file_list:
        file_name = re.search(r"/([^/]+)\.csv$", file).group(1)
        df = pd.read_csv(file)
        data = df.to_dict(orient='records')

        Mongo().post_data(collection=file_name, data=data)


if __name__ == "__main__":
    data_to_mongo()
