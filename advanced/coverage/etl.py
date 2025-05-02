import os
from typing import List
def clean_data(data):
    return [x.strip().lower() for x in data if x]

def print_o(msg):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(msg)

def clean_data_title(data: List[str]):
    return [x.strip().title()  for x in data if x ]