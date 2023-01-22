import pymongo
import pandas as pd
import numpy as np
import os, sys
from dataclasses import dataclass


@dataclass
class EnvironmentVariable:
    mongo_db_url=os.getenv("MONGO_db_URL")

env_var=EnvironmentVariable()
mongo_client=pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN="expenses"
print(f"{env_var.mongo_db_url}")
