import uvicorn as uvicorn
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from sqlmodel import Session, select
from typing import List
from sqlmodel import SQLModel, create_engine, Field
from typing import Optional
import os

from fastapi import FastAPI, Request, File, UploadFile, BackgroundTasks
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="frontend")

#for connecting front end (optional)⬇️⬇️⬇️
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
#for connecting front end (optional)⬆️⬆️⬆️


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

conn_str = 'sqlite:///' + os.path.join(BASE_DIR, 'books.db')
print(conn_str)

engine = create_engine(conn_str, echo=True)

print("CREATING DATABASE.....")

SQLModel.metadata.create_all(engine)


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ans: str


print("CREATING DATABASE.....")

SQLModel.metadata.create_all(engine)

session = Session(bind=engine)


@app.get('/books', response_model=List[Book],
         status_code=status.HTTP_200_OK)
async def all_ans_teacher_provided():
    statement = select(Book)
    results = session.exec(statement).all()

    return results


@app.post('/books', response_model=Book,
          status_code=status.HTTP_201_CREATED)
async def post_ans(book: Book):
    new_book = Book(ans=book.ans)

    session.add(new_book)

    session.commit()

    return new_book


@app.get('/book/{book_id}', response_model=Book)
async def get_ans_by_id(book_id: int):
    statement = select(Book).where(Book.id == book_id)


    result = session.exec(statement).first()

    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result


@app.put('/book/{book_id}', response_model=Book)
async def update_ans(book_id: int, book: Book):
    statement = select(Book).where(Book.id == book_id)

    result = session.exec(statement).first()

    result.ans = book.ans

    session.commit()

    return result


@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_ans(book_id: int):
    statement = select(Book).where(Book.id == book_id)

    result = session.exec(statement).one_or_none()

    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Resource Not Found")

    session.delete(result)

    return result
if __name__== "__main__":
    uvicorn.run(app, host='localhost', port=5500)