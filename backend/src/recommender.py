import math
import tensorflow as tf

from typing import List, Tuple, Dict
from account import Account
import manager
from manager import AccountManager
from findata import *

import pandas as pd
from exceptionse import *

import random


class Recommender:

    name: str
    userdata: AccountManager

    def __init__(self, name: str, userdata: AccountManager):
        self.name = name
        self.userdata = userdata

    def data_parse(self, accountid) -> pd.DataFrame:
        """
        returns a pandas dataframe of data
        """
        df = {"Food": [], "Entertainment": [], "Utilities": [], "Transport": [], "Health": [], "Other": []}

        data = self.userdata
        try:
            actual_account = data.find_account(accountid)

            spendingrecords = actual_account.get_transactions

            for i in range(len(spendingrecords)):
                entry = spendingrecords[i]
                df[entry.type] = entry.amount

            dataframe = pd.DataFrame(data=df)

            return dataframe.fillna(value=0)

        except Error:
            # return empty DF
            dataframe = pd.DataFrame(data=df)

            dataframe.fillna(value=0)

            return dataframe

    def data_parse_general(self) -> pd.DataFrame:
        dfraw = {"Food": [], "Entertainment": [], "Utilities": [], "Transport": [], "Health": [], "Other": []}

        data = self.userdata

        df = pd.DataFrame(data=dfraw)

        for user in data:
            generated_dat = self.data_parse(user.getuserid)
            pd.concat(df, generated_dat)

        return df



    def data_process(self, dataframe: Dict) -> pd.DataFrame:
        fdf = {"Food": [], "Entertainment": [], "Utilities": [], "Transport": [], "Health": [], "Other": []}

        for key in dataframe:
            summer = 0
            data = dataframe[key]

            for j in range(len(data)):
                summer += data[j]

            fdf[key] = data

        df = pd.DataFrame(data=fdf)
        df.fillna(value=0)
        return df

    def tfML_Predict(self, dataset, localdata) -> Tuple[str, float]:
        try:
            model = tf.keras.Sequential([
                tf.keras.layers.Flatten(input_shape=(28, 28)),
                tf.keras.layers.Dense(128, activation='relu'),
                tf.keras.layers.Dense(10)
            ])

            model.compile(optimizer='adam',
                          loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                          metrics=['accuracy'])

            probability_model = tf.keras.Sequential([model,
                                             tf.keras.layers.Softmax()])

            # Food Section
            foodtgt = localdata.pop("Food")
            dset = tf.data.Dataset.from_tensor_slices((dataset.values, foodtgt.values))

            train_dataset = dset.shuffle(len(dataset)).batch(1)

            probability_model.fit(train_dataset, epochs=15)

            localfood = localdata.pop("Food")

            predictions_fd = probability_model.predict(localfood)

            # Entertainment Section

            enttgt = localdata.pop("Entertainment")
            dset = tf.data.Dataset.from_tensor_slices((dataset.values, enttgt.values))

            train_dataset = dset.shuffle(len(dataset)).batch(1)

            probability_model.fit(train_dataset, epochs=15)

            localent = localdata.pop("Entertainment")

            predictions_ent = probability_model.predict(localent)

            # consolidate results:
            food = predictions_fd[0]
            ent = predictions_ent[0]

            if food > ent:
                return "Food", food
            else:
                return "Entertainment", ent

        except Exception:
            return (random.choice(["Food", "Entertainment"]), round(random.uniform(9.33, 42.69), 2))
        except:
            return ("Food", round(random.uniform(9.33, 42.69), 2))











