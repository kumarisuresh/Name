from textblob import TextBlob#install textblob before importing
import PyPDF2 #install PyPDF2 before using
l=[]#empty list
print("Content of the document:")
pdfFileObj = open('Naveen_Corporate_Trainer.pdf', 'rb')#opening the file
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)#creating object of the file
#print(pdfReader.numPages)This will be used to print the total number of pages in the console which is used in for loop to traverse the document
for i in range(0,pdfReader.numPages):
     pageObj = pdfReader.getPage(i)#getting the page
     print(pageObj.extractText()) #extract the text
     blob=TextBlob(pageObj.extractText())#pass the text as a object to TextBlob
     for words, tag in blob.tags:
          if tag=='JJ' or tag=='NNP':
               l.append(words)#creating the list of noun and adjective and storing it in a list and later printing the first 3 values of the list since the name will be in the begining of the resume
print("Name of the document:",l[0],l[1],l[2])#print the name
               
