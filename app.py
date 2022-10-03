import math
from flask import Flask,jsonify,request
import json


app=Flask(__name__)

@app.route('/',methods=['GET'])
def ola_mundo():
    return {"Ola":"Ola mundo"}


@app.route('/calcular', methods=['POST'])
def postCalcular():

    body = json.loads(request.data)

    hpt=float(body['hipotenusa'])
    co=float(body['catetooposto'])
    ca=float(body['catetoadjacente'])

    if ca>co and hpt==0:
        res = pow(ca,2)+pow(co,2)
        body["hipotenusa"]= res
    elif hpt>ca and co==0:
        res = pow(hpt,2)-pow(ca,2)
        body["catetooposto"]= res
    elif hpt>co and ca==0:
        res = pow(hpt,2)-pow(co,2)
        body["catetoadjacente"]= res
    else:
        res='Verifique os dados e tente novamente'

    body["resultado"]=res

    return body


if __name__ == "__main__":
    app.run(debug=True)


