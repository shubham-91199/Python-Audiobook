import pyttsx3
import PyPDF2
book = open('26623152.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

#the (2,pages) in below line denotes 
#(indexing page,all the pages).i.e.all the pages starting from page 3 will be read out
for num in range(2, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

