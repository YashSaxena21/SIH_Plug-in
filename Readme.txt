                                                      Plug-In for Diksha App

-About the Plug-In:-
 The plug-in is designed to assist/help the teachers to assess the performance of the class using our OCR model and we also 
 provide various visuals to the teacher to understand the performance of class in an easy manner.

- How it works:-
   The students will be provided with printed card-boards with their roll numbers and options, which they can chhose from to
   answer the question(even works with text written on digital screens). 

   The teacher will click the picture of the students with answers written on cardboards. The model will recognise the text written
   on the cardboard and will tag the answer against the their IDs.

   This will help the teacher to identify that which student has given the right answer and which student has given the wrong answer.
   This can even be displayed using charts and graphs.

Tech Stack:-

- OCR (Optical Character Recognition) Model:-

1) Keras-OCR is used as the OCR Model, the Keras OCR library's Detector is trained on CRAFT model and it's recognizer is trained on 
     kurapan.h5 model.
2) The model is further trained/processed to compeletly fulfill the problem statement's need.
3) The Keras-OCR model is better than Google's Tesseract, EasyOCR, SimpleOCR and many more when it comes to fetching characters
     from the real environment and is in par with most of the paid OCR models like Amazon's Textract etc.

- Back-end, Database and Front-end:-

1) FastAPI is used for the back-end (which is compatible with Sunbird, on which the Diksha app is built and SQLite is used as the 
    database.
2) HTML, CSS, JavaScript and React.js is used for the front-end part (for demonstrational purposes).  

( Folders: )

1)	BACKEND_APIs_&_DATABASE: 
2)	FRONTEND
3)	API_model
4)	Juypiter_Notebook_Model(OCR)

