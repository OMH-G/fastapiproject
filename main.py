from fastapi import FastAPI,Query,Path
from enum import Enum
from pydantic import BaseModel
from typing import Optional
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

# @app.get('/items')
# async def list_items():
fake_db=['alsdkf','asdfk','aslkdfsdflaskdf']
@app.get('/items')
def list_items(skip:int=0,limit:int=4):
    return fake_db[skip:skip+limit]

class Item(BaseModel):
    name:str 
    desc:Optional[str]=None 
    price:float 
    tax:Optional[float]=None

@app.post('/items')
def create_item(item:Item):
    item_dictionary=item.dict()

    return item_dictionary


#when three dots are present then it means that it is required .
#in request ?q=asd&?q=sdk -> then here sdk is stored in q if we want to store list of values then we have to use List[str]

@app.get('/items')
async def read_items(q: Optional[str]=Query(...,max_length=4)):
    res={'items':[{'items':'foo'},{'items':'bar'}]}
    if(q):
        res.update({'q':q})
    return res 
# @app.get('/items')
# async def read_items(q:Optional[str]=Query(None,max_length=4)):
#     res={'items':[{'items':'foo'},{'items':'bar'}]}
#     if(q):
#         res.update({'q':q})
#     return res 
@app.get('/items_validation/{item_id}')
def read_items_validation(
    q:str,
    item_id:Optional[int]=Path(...,title='The ID of the item to get',gt=4),
    # q:Optional[str]=Query(None,alias='Item-Query')
    ):
    res={'item_id':item_id}
    if(q):
        res.update({'q':q})
    return res 
