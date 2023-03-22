import datetime
import pandas as pd

def cadena(excel):
    alumnos = []
    value = ""

    colums = ['VERSION','FOLIO_CONTROL','CURP_RESPONSABLE','ID_CARGO','CARGO','ABR_TITULO','CVE_INSTITUCIONAL','NOMBRE_INSTITUCION','CVE_CARRERA','NOMBRE_CARRERA','FECHA_INICIO','FECHA_TERMINACION','ID_AUTORIZACION_RECONOCIMIENO','AUTORIZACION_RECONOCIMIENO','NUMERO_RVOE','CURP_PROFESIONISTA','NOMBRE','PRIMER_APELLIDO','SEGUNDO_APELLIDO','CORREO_ELECTRONICO','FECHA_EXPEDICION','ID_MODALIDAD_TITULACION','MODALIDAD_TITULACION','FECHA_EXAMEN_PROFESIONAL','FECHA_EXENCION_EXAMEN_PROFESIONAL','CUMPLIO_SERVICIO_SOCIAL','ID_FUNDAMENTO_LEGAL_SERVICIO_SOCIAL','FUNDAMENTO_LEGAL_SERVICIO_SOCIAL','ID_ENTIDAD_FEDERATIVA','ENTIDAD_FEDERATIVA','INSTITUCION_PROCEDENCIA','ID_TIPO_ESTUDIO_ANTECEDENTE','TIPO_ESTUDIO_ANTECEDENTE','ID_ENTIDAD_FEDERATIVA','ENTIDAD_FEDERATIVA','FECHA_INICIO_PROCEDENCIA','FECHA_TERMINACION_PROCEDENCIA','NO_CEDULA']
    data = pd.read_excel(excel)
    df = pd.DataFrame(data,columns=colums)
    fecha = datetime.datetime.now()
    fecha = str(fecha.day)+'-'+str(fecha.month)+'-'+str(fecha.year)+'-'+str(fecha.hour)+':'+str(fecha.minute)
    f = open (f'./cont/cadena_{fecha}.txt','w')
    for row in df.itertuples():

        if pd.isna(row.SEGUNDO_APELLIDO):
            SEGUNDO_APELLIDO = ''
        else:
            SEGUNDO_APELLIDO = row.SEGUNDO_APELLIDO
        #-------------------------------------------
        if pd.isna(row.NUMERO_RVOE):
            NUMERO_RVOE = ''
        else:
            NUMERO_RVOE = row.NUMERO_RVOE
        #-------------------------------------------
        if pd.isna(row.NO_CEDULA):
            NO_CEDULA = ''
        else:
            NO_CEDULA = row.NO_CEDULA
        #-------------------------------------------
        if pd.isna(row.FECHA_EXAMEN_PROFESIONAL):
            FECHA_EXAMEN_PROFESIONAL = ''
        else:
            FECHA_EXAMEN_PROFESIONAL = (row.FECHA_EXAMEN_PROFESIONAL.to_pydatetime()).date()
            
        value = f'||{row.VERSION}|{row.FOLIO_CONTROL}|{row.CURP_RESPONSABLE}|{row.ID_CARGO}|{row.CARGO}|{row.ABR_TITULO}|{row.CVE_INSTITUCIONAL}|{row.NOMBRE_INSTITUCION}|{row.CVE_CARRERA}|{(row.FECHA_INICIO.to_pydatetime()).date()}|{(row.FECHA_TERMINACION.to_pydatetime()).date()}|{row.ID_AUTORIZACION_RECONOCIMIENO}|{row.AUTORIZACION_RECONOCIMIENO}|{NUMERO_RVOE}|{row.CURP_PROFESIONISTA}|{row.NOMBRE}|{row.PRIMER_APELLIDO}|{SEGUNDO_APELLIDO}|{row.CORREO_ELECTRONICO}|{(row.FECHA_EXPEDICION.to_pydatetime()).date()}|{row.ID_MODALIDAD_TITULACION}|{row.MODALIDAD_TITULACION}|{FECHA_EXAMEN_PROFESIONAL}|{(row.FECHA_EXENCION_EXAMEN_PROFESIONAL.to_pydatetime()).date()}|{row.CUMPLIO_SERVICIO_SOCIAL}|{row.ID_FUNDAMENTO_LEGAL_SERVICIO_SOCIAL}|{row.ID_ENTIDAD_FEDERATIVA}|{row.ENTIDAD_FEDERATIVA}|{row.INSTITUCION_PROCEDENCIA}|{row.ID_TIPO_ESTUDIO_ANTECEDENTE}|{row.TIPO_ESTUDIO_ANTECEDENTE}|{row.ID_ENTIDAD_FEDERATIVA}|{row.ENTIDAD_FEDERATIVA}|{(row.FECHA_INICIO_PROCEDENCIA.to_pydatetime()).date()}|{(row.FECHA_TERMINACION_PROCEDENCIA.to_pydatetime()).date()}|{NO_CEDULA}||'
        f.write(row.NOMBRE+'\n'+value+'\n'+'\n')
    f.close()

    return df
