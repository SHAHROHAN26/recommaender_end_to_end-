# Script to get project folder structure 

import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(messages)s"
)

while True:
    Project_Name= input("Enter your project name :")
    if Project_Name !='':
        break
logging.info("creating project by name:",Project_Name)

list_of_file=[
    ".github/workflow/.gitkeep",
    ".github/workflow/main.yaml",
    f"{Project_Name}/__init__.py",
    f"{Project_Name}/components/__init__.py",
    f"{Project_Name}/entity/__init__.py",
    f"{Project_Name}/pipeline/__init__.py",
    f"{Project_Name}/logger/__init__.py",
    f"{Project_Name}/config.py",
    f"{Project_Name}/exception.py",
    f"{Project_Name}/predictor.py",
    f"{Project_Name}/utils.py",
    f"configs/config.yaml",
    "requirement.txt",
    "setup.py",
    "main.py"
    #"data_dump.py",
    #"README.md"
    
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating new directory at: {filedir} for file : {filename}")
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating ne file: {filename} for file path: {filepath}")
    else:
        logging.info(f"file already exsist at path: {filepath}")
            