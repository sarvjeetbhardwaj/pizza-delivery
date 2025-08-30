from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

secret_token =  os.getenv('secret_token')

class SignUpModel(BaseModel):
    username : str
    password : str
    email : str
    is_staff : Optional[bool]
    is_active: Optional[bool]

    class Config:
        from_attributes=True
        json_schema_extra = {
            'example':{
                'username': 'johndoe',
                'email': 'johndoe@gmail.com',
                'password' : 'password',
                'is_staff' : False,
                'is_active': True
            }

        }


class Settings(BaseModel):
    authjwt_secret_key:str = secret_token