db2 = [
    {
        "name": "John",
        "age": 30
    },
    {
        "name": "Jane",
        "age": 25
    },
]
import json
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

response = supabase.table('users').select("*").execute()



def say_hello():
    return "This is the API for the api boiler app"


def get_users():

    # print(response)
    return response
