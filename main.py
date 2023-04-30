from fastapi import FastAPI
from enum import Enum
app=FastAPI()
@app.get('/')
async def root():
    return {'message':'Hello worlsdd'}
@app.post('/')
async def poster():
    return {'message':'Post requesdt'}

@app.put('/')
async def put():
    return {'message':'PUut'}


#Here checking takes place by line wise hence if it gets match before then it will match and return response .
#Hence we have to specify the type of data which we are passsing 
@app.get('/item/me')
def getitem():
    return {'message':'Omkar'}
@app.get('/item/{itemid}')
def getitem(itemid:int):
    return {'message':itemid} 

class FoodEnum(str,Enum):
    fruits='fruits'
    vegetable='vegetable'
    dairy='dairy'

@app.get('/foods/{food_name}')
def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetable:
        return {'foodName':food_name}
    elif food_name==FoodEnum.fruits:
        return {'foodName':food_name}
    elif food_name==FoodEnum.dairy:
        return {'foodName':food_name}
