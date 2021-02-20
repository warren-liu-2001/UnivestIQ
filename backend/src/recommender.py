import math
import tensorflow as tf

from typing import List, Tuple, Dict
from account import Account
import manager
from manager import AccountManager

import pandas as pd


class Recommender:

    name: str
    userdata: AccountManager

    def __init__(self, name, userdata):
        self.name = name
        self.userdata = userdata










