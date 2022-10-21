from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import keras_ocr
import pandas as pd

app = FastAPI()


@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
        pipeline = keras_ocr.pipeline.Pipeline()
        image = read_file_as_image(await file.read())
        prediction = pipeline.recognize(image)
        a = []
        predicted_image_1 = prediction[0]
        for text, box in predicted_image_1:
            a.append(text)
        b = []
        c = []
        j = 0
        x = 1
        for text, box in predicted_image_1:
            if ('x' in text):
                character = ""
                number = ""
                for i in text:
                    if (i == 'x'):
                        j = 1
                        continue
                    if (j == 0):
                        if (i.isdigit() or i == 'b' or i == 'o' or i == 'i' or i == 'z' or i == 's'):
                            if (i == 'b'):
                                i = '6'
                            if (i == 'o'):
                                i = '0'
                            if (i == 'i'):
                                i = '1'
                            if (i == 'z'):
                                i = '3'
                            if (i == 's'):
                                i = '5'
                        number += i
                    elif (j == 1):
                        character += i
                    if (i == text[-1]):
                        b.append(number)
                        c.append(character)
                        j = 0
        df = pd.DataFrame(list(zip(b, c)), columns=["RollNo.", "Answer"])
        df.to_csv("temp1.csv", index=False)
@app.get("/ping")
async def ping():
    return "Hello, I am alive"


if __name__=="__main__":
    uvicorn.run(app, host='localhost', port=8000)
