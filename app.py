from fastapi import FastAPI, Request, HTTPException
app = FastAPI()

tanks = [
    {
      "id": 11,
        "location":"engineeringdpt",
        "lat":"51.5551",
        "long":"0.1084"
    },
    {
        "id": 12,
        "location":"Physicsdpt",
        "lat":"53.4631",
        "long":"2.2913"
    },
    {
        "id": 13,
        "location":"Compdpt",
        "lat":"53.4832",
        "long":"2.2004"
    },
    {
        "id": 14,
        "location":"Biodpt",
        "lat":"51.6042",
        "long":"0.0662"
    },
    {
        "id": 15,
        "location":"Chemdpt",
        "lat":"51.4817",
        "long":"0.1910"
    }
]

@app.get("/tank")
def get_all_tanks():
    return tanks

@app.patch("/tank/{tank_id}")
async def partially_alter_tank(tank_id: int, request: Request):
    alter_tank = await request.json()
    
    for i, tank in enumerate(tanks):
        if tank["id"] == tank_id:
            tanks[i] = {**alter_tank,**tank}
            return tanks[i]
        raise HTTPException(status_code=404, detail=" tank with id:"+ tank_id +" not found") 
    
@app.delete("/tank/{tank_id}")
def delete_tanks(tank_id:int):
    tank_index = 0
    for i in range (len(tanks)):
       if tanks[i]["id"]== id:
         tank_id= id
         break
    del tanks[tank_index]
    return{
        "tank deleted succesfully"
    }

@app.post("/tank/", status_code =201)
async def post_tank(tank_id: int, request: Request):
    post_tank = await request.json()
    
    
    tank["id"] == tank_id
    tanks = {**post_tank,**tank}
    return (tanks)
        




