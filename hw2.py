from pydantic import BaseModel, EmailStr, Field, model_validator, field_validator
import json


class Address(BaseModel):
    city: str = Field(...,min_length=2)
    street: str = Field(...,min_length=3)
    house_number: int = Field(...,gt=0)

class User(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=0, lt=100)
    email: EmailStr
    is_employed: bool = Field(...)
    address: Address = Field(...)

    @model_validator(mode='after')
    def check_employment_status(self):
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError("Employment status must be between 18 and 65")
        return self

    @field_validator('name')
    @classmethod
    def check_name(cls, value):
        name = value.replace(' ', '')
        if not name.isalpha():
            raise ValueError('The name must contain letters only!!')
        return value




json_input = """{

    "name": "John Doe",

    "age": 70,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""


andry = """{

    "name": "Andry Doe",

    "age": 54,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""

alisa = """{

    "name": "Alisa1 Doe",

    "age": 33,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""

def checker_json(file: str):
    file_dict = json.loads(file)
    if User(**file_dict):
        return file
    return None


try:
    print(checker_json(json_input))
except Exception as e:
    print(e)

try:
    print(checker_json(andry))
except Exception as e:
    print(e)

try:
    print(checker_json(alisa))
except Exception as e:
    print(e)