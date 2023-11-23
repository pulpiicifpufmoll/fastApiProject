# Protocolo HTTP:       https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipert exto
# Autenticació HTTP:    https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml
#                       https://developer.mozilla.org/es/docs/Web/HTTP/Authentication
# Path parameters:      https://fastapi.tiangolo.com/tutorial/path-params/
# Query parameters:     https://fastapi.tiangolo.com/tutorial/query-params/
# Resquest body:        https://fastapi.tiangolo.com/tutorial/body/
# Anotated types:       https://stackoverflow.com/questions/71898644/how-to-use-python-typing-annotated
#                       https://fastapi.tiangolo.com/python-types/#type-hints-with-metadata-annotations
#                       https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#advantages-of-annotated
# pydantic:             https://docs.pydantic.dev/2.0/
# Cookies               https://clearcode.cc/blog/browsers-first-third-party-cookies/
# Diferencias Browsers: https://caniuse.com/?search=cookie
# Tutorial completo:    https://www.tutorialspoint.com/fastapi/fastapi_cookie_parameters.htm#:~:text=To%20read%20back%20the%20cookie,object%20in%20the%20FastAPI%20library.&text=Inspect%20these%20two%20endpoints%20in,bound%20to%20%22%2Fcookies%22. 
# Enviar json/javascript: https://developer.mozilla.org/en-US/docs/Web/API/fetch

# Permite crear un backend de una aplicación web
import requests

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Carpeta estática habilitada para archivos estáticos como el HTML o CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# URL de open data del govern de les Illes Balears

apiUrl = "https://catalegdades.caib.cat/api/id/h63j-8h6m.json"

# -- GETs METODEs --
@app.get("/")
async def root():
    return FileResponse("./static/main.html", media_type="text/html")


@app.get("/playas/municipio/{municipio}")
async def getBeachByMunicipality(municipio: str):
    response = requests.get(apiUrl + "?municipi=" + municipio)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error en la solicitud HTTP"}

@app.get("/playas")
async def getBeachByIsland(isla: str = None):
    response = requests.get(apiUrl + "?illa=" + isla)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error en la solicitud HTTP"}

@app.get("/playas-total")
async def getAllBeaches():
    response = requests.get(apiUrl)

    if response.status_code == 200:
        return response.json()  
    else:
        return {"error": "Error en la solicitud HTTP"}

# -- MONTAR EL APP EN UVICORN DIRECTAMENTE
# print()
# if __name__ == "__main__":
#     print("-> Inicio integrado de servicIo web")
#     uvicorn.run("main:app", port=8000, reload=True)
# else:
#     print("=> Iniciado desde el servidor web")
#     print("   Módulo python iniciado:", __name__)