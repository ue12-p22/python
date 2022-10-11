import requests
import numpy as np
from typing import *

penguin=r"""    \              
     \  .--.       
       |o_o |      
       ||_/ |      
      //   \ \     
     (|     | )    
    /'\_   _/'\    
    \___)=(___/    
"""


ERROR_MESSAGE = "No joke found. :("

def get_chuck_norris_joke() -> str:
    response = requests.get('http://api.icndb.com/jokes/random', timeout=0.2).json()
    if response['type'] == "success":
        return response['value']['joke']
    return ERROR_MESSAGE
    print(ERROR_MESSAGE)

def get_kaamelott_joke() -> str:
    a=1
    response = requests.get("https://kaamelott.chaudie.re/api/random", timeout=0.2).json()
    if response['status'] == 1:
        data = response['citation']
        return f"{data['citation'].strip()}\n{data['infos']['personnage']} ({data['infos']['saison']})"
    else:
        return ERROR_MESSAGE
    print("End")
    


def display(msg, width:int = 40, HEADER: List[str] = []) -> None:
    from textwrap import wrap

    list = wrap(msg, width=width)
    print('\n'.join(HEADER))
    print(f" +{'-'*(width+2)}+")
    for line in list:
        print(f" | {line:^40} |")
    print(f" +{'-'*(width+2)}+")
    print(penguin)


if __name__ == '__main__':
    from sys import argv, path
    JOKES_APIS = {
        'chuck-norris': get_chuck_norris_joke,
        'kaamelott': get_kaamelott_joke
    }

    joke = argv[1]
    try:
        display(JOKES_APIS[joke](), HEADER=[f"You asked for a {joke} joke", "--\n"])
    except:
        display(f"Authorized jokes : {', '.join(JOKES_APIS.keys())}. You gave"
                f" {joke}.")
        pass

    print(a)


