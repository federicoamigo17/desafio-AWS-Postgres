import boto3
import os

# Esto esta comentado en detalle en el jupyter


# Para el desafio lo que hice fue guardar los SECRETS que me dieron como variable de entorno, actualmente subi los cvs a un bucket en s3
KEY = os.environ.get('XXX')
SECRET = os.environ.get('XXX')

#Recordar que los secret estaban definidos como variables de entorno
def descargar(bucket, key):
    """
    Descarga un archivo desde el servicio AWS S3 usando boto3.

    Parámetros:
    - bucket: el nombre del bucket de S3 donde se encuentra el archivo.
    - key: el identificador del archivo dentro del bucket.
    - filename: el nombre del archivo local donde se guardará el archivo descargado.

    Retorna:
    - El nombre del archivo local si se ha descargado correctamente, o None en caso contrario.
    """
    # Crear un cliente con las credenciales
    s3 = boto3.client('s3', aws_access_key_id=KEY, aws_secret_access_key=SECRET)
    # Intentar descargar el archivo desde el bucket y el key especificados
    
    # Creo el nombre del archivo local a partir del key
    filename = os.path.basename(key)

    #Verifico si el archivo ya existe y si es asi lo borro
    if os.path.exists(filename):
        os.remove(filename)
    
    try:
        with open(filename, 'wb') as f:
            s3.download_fileobj(bucket, key, f)
            # Retorno el nombre del archivo descargado
            print(f'Archivo {filename} descargado correctamente.')
            return filename
    except Exception as e:
        # Mostrar un mensaje de error con la excepción ocurrida
        print(f'Error al descargar el archivo: {e}')
        # Retornar None si ocurre una excepción
        return None

#Aca genero la lista de keys que quiero descargar
bucket = 'federicoamigo17portfolio'
keys = ['disney_plus_titles.csv', 'netflix_titles.csv']

#* Descargar los archivos desde el bucket desafio-rkd (tener en cuenta que si se pasa un tercer parametro se sigue pudiendo modificar el nombre del archivo).

for key in keys:
    descargar(bucket, key)