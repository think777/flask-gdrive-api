from flask import Flask, request,jsonify
from demo import *
from abc import *
from flask_cors import CORS, cross_origin

import PyPDF2

from csv import writer
import json
  

def getDecDeets(f11):
    l = []
    with open(f11, "rb") as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for i in range(number_of_pages):
            page = read_pdf.pages[i]
            #print(page)
            page_content = page.extractText()
            x = page_content
            #print(x)
            l.append(x.split())
    y = l
    #print(x)
    x = l[0]
    #print(x)

    i = 0
    while x[i] != "NAME":
        x.remove(x[i])
    #print(x)

    student_name = ""
    parent_name = ""
    student_srn = ""
    student_phno = ""
    student_mail = ""
    parent_phno = ""
    student_gpa = ""
    parent_mail = ""
    j = 0
    a1 = x.index("SRN")
    a2 = x.index("STUDENT")
    l1 = []
    d = {}
    if a2 - a1 == 2:
        student_name = x[1] + x[2]
        student_srn = x[4]
        student_phno = x[7]
        student_mail = x[10]
        parent_name = x[13] + x[14]
        parent_phno = x[17]
        parent_mail = x[20] + x[21]
        d['student_name'] = student_name
        d['student_srn'] = student_srn
        d['student_phno'] = student_phno
        d['student_mail'] = student_mail
        d['parent_name'] = parent_name
        d['parent_phno'] = parent_phno
        d['parent_mail'] = parent_mail
        # print(l1)

    else:
        student_name = x[1] + x[2]
        student_srn = x[4] + x[5]
        student_phno = x[8] + x[9]
        student_mail = x[12]
        parent_name = x[15] + x[16]
        parent_phno = x[19] + x[20]
        parent_mail = x[23] + x[24] + x[25]
        d['student_name'] = student_name
        d['student_srn'] = student_srn
        d['student_phno'] = student_phno
        d['student_mail'] = student_mail
        d['parent_name'] = parent_name
        d['parent_phno'] = parent_phno
        d['parent_mail'] = parent_mail
        # print(l1)
    
    return(json.dumps(d))


# Initializing flask app
app = Flask(__name__)
  
cors = CORS(app)  
app.config['CORS_HEADERS'] = 'Content-Type'

# Route for seeing a data
@app.route('/dec', methods=['GET'])
def declaration():
    args = request.args
    k = args.get("foldername")
    down(k)
    i = getDecDeets(k)
    return i

@app.route('/misc', methods=['GET'])
def key():
    args = request.args
    k = args.get("filename")
    i = show(k)
    return i
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)