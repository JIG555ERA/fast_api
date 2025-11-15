from fastapi import APIRouter
from bson import ObjectId
from database import collection
from models.user import User

router = APIRouter()

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/")
async def create_user(user: User):
    user_dict = user.dict()
    result = await collection.insert_one(user_dict)
    created = await collection.find_one({"_id": result.inserted_id})
    return serialize_doc(created)

@router.get("/")
async def get_users():
    users = await collection.find().to_list(100)
    return [serialize_doc(u) for u in users]
