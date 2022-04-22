import requests
import json



"""
--------------------------Prueba de diccionarios
url = "https://api.fbi.gov/wanted/v1/list"
response = requests.get(url)

if response.status_code==200:
    informacion = response.json()
    #print(informacion)
    for i in informacion:
        #print(i+""+str(informacion[i]))
        #print("**********************************")
        items = informacion.get('items')
        for j in items:
            nombre = j.get('aliases')
                
            try:
                if nombre:
                    print(nombre[0])
            except:
                print("No hay nombre disponible")
        #print(informacion['pages'])


----------------------------   .get con parametros 
url = "http://httpbin.org/get"
params = {'Juana':'Echeverry', 'Maria':'Gomez','Brian':'Restrepo'}
r =requests.get(url, params=params)
print(r.json())
if r.status_code == 200:
    #print(r.text)
    #print(r.encoding)
    #print(r.content)
    #infomracion = r.json()
    #print(infomracion)
    pass


-------------------------     .post con headers


url = 'http://httpbin.org/post'
pyload = {'some':'data'}
headres = {'content-type':'applications/json'}
r = requests.post(url,data=json.dumps(pyload),headers=headres)
print(r.text)


---------------------------      .post con la data

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

----------------------------      .post con file
LEERA LA INFIORMACION DE LO QUE VA POR EL SERVIDOR
url = 'http://httpbin.org/post'
files = {'file':open('informacion.csv','rb')}
r = requests.post(url,files=files)
print(r.text)

-----------------------------       .post con file y caracteres de cadena
LEERA LA INFIORMACION Y UN ARCHIVO ANEXO
url = 'http://httpbin.org/post'
files = {'file':('informacion.csv','informaicon que se enviara de otra forma con archivos')}
r = requests.post(url,files=files)
print(r.text)
"""






"""
informacion impotante:
.text --> Lee respuestas en formato json
.encoding --> Muestra el utf-8
.content --> Muestra el contenido en texto python 
"""