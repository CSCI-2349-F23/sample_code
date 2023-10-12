import docx
import sys

# Word doc you are interested in
myfile = sys.argv[1]

# Read it in wiht docx library
doc = docx.Document(myfile)

# It grabs every paragraph, so just print each one out.
for para in doc.paragraphs:
    print(para.text)




