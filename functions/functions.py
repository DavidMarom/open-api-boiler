import json
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)


def say_hello():
    return "This is the API for the api boiler app"


def get_users():
    return supabase.table('users').select("*").execute().data


def get_user_by_id(id):
    return supabase.table('users').select("*").eq('id', id).execute().data


def create_user(body):
    return supabase.table('users').insert(body).execute().data


def update_user(id, body):
    return supabase.table('users').update(body).eq('id', id).execute().data


def delete_user(id):
    return supabase.table('users').delete().eq('id', id).execute().data
