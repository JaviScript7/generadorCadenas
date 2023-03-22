import io
import os 
from os import remove
from flask import Flask,flash, render_template, request, send_file,redirect
import pandas as pd
from excel import cadena

FILE_CONTAINER = './cont/'

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FILE_CONTAINER'] = FILE_CONTAINER


@app.route('/')
def index():
    dir = FILE_CONTAINER
    with os.scandir(dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    return render_template("index.html", ficheros=ficheros)

@app.route('/procesar',  methods=['POST'])
def procesar():
    colums1 = ['CARRERA','NOMBRE','CALIFICACION']
    excel = request.files.get("excel")
    #data1 = pd.read_excel(excel,sheet_name='ACTA')
    #df1 = pd.DataFrame(data1,columns=colums1) 
    data = cadena(excel)
    print(data)
    return redirect('/')
    
#Esta funcion permite descargar los archivos
@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = FILE_CONTAINER + filename
    print(file_path)
    return send_file(file_path, as_attachment=True, download_name=filename)

#Esta es la funcion que se encarga de la eliminacion de los archivos 
@app.route('/removefile/<filename>')
def remove_file(filename):
    file_path = FILE_CONTAINER + filename
    remove(file_path)
    print("Archivo eliminado con exito")
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)