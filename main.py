from fastapi import FastAPI
from pydantic import BaseModel  # New import
import mysql.connector

app = FastAPI()

# Connect E40DB ----------------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
    host="163.50.57.96",
    user="admin",
    password="conDB!@#$%",
    database="mt900"
)
print("Connented to E40DB ", mydb)

# book_db = [
#     {
#         "title":"The C Programming",
#         "price": 720
#     },
#     {
#         "title":"Learn Python the Hard Way",
#         "price": 870
#     },
#     {
#         "title":"JavaScript: The Definitive Guide",
#         "price": 1369
#     },
#     {
#         "title":"Python for Data Analysis",
#         "price": 1394
#     },
#     {
#         "title":"Clean Code",
#         "price": 1500
#     },
# ]

# Model ------------------------------------------------------------------------------------------------------
# class Book(BaseModel):
#     title: str
#     price: float


class TwoMask(BaseModel):
    front_pos: str
    front_width: str
    back_pos: str
    back_width: str

# Route ------------------------------------------------------------------------------------------------------
# create new book
# @app.post("/book")
# async def create_book(book: Book):
#     book_db.append(book.dict())
#     return book_db[-1]

# @app.get("/gbook")
# async def get_book():
#     return book_db


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/twom")
async def get_twom():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM twomask_cpk")
    myresult = mycursor.fetchall()
    return myresult


@app.post("/twom/")
async def create_twom(twom: TwoMask):
    data_new = [
        twom.front_pos,
        twom.front_width,
        twom.back_pos,
        twom.back_width,
    ]
    mycursor = mydb.cursor()
    mycursor.execute(
        "INSERT INTO twomask_cpk (front_pos,front_width,back_pos,back_width) VALUES (%s,%s,%s,%s,%s)", data_new)
    mydb.commit()
    return data_new
