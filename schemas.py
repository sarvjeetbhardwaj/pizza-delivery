from pydantic import BaseModel
from typing import Optional

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
    authjwt_secret_key:str = '829e62d8cce82e22f8d8874372cdade5e6b26254fb7662b3095908a36ee0ee88'