import boto3
import os
import sys

# Lee el bucket desde la variable de entorno o usa valor por defecto
INPUT_BUCKET = os.getenv("INPUT_BUCKET", "upeu-producer-x-bucket-1")
FILE_PATH = sys.argv[1] if len(sys.argv) > 1 else None

if not INPUT_BUCKET:
    print("❌ INPUT_BUCKET no está definido. Revisa tus variables de entorno.")
    sys.exit(1)

if not FILE_PATH:
    print("❌ Debes proporcionar el path del archivo CSV.")
    sys.exit(1)

if not FILE_PATH.endswith('.csv'):
    print("❌ Solo se permiten archivos .csv")
    sys.exit(1)

s3 = boto3.client("s3")

# Verifica si el bucket existe
try:
    s3.head_bucket(Bucket=INPUT_BUCKET)
    print(f"✅ Bucket '{INPUT_BUCKET}' verificado.")
except s3.exceptions.ClientError as e:
    print(f"❌ El bucket '{INPUT_BUCKET}' no existe o no tienes acceso.")
    print(e)
    sys.exit(1)

# Sube el archivo al bucket
try:
    file_name = os.path.basename(FILE_PATH)
    s3.upload_file(FILE_PATH, INPUT_BUCKET, f"uploads/{file_name}")
    print(f"✅ Archivo '{file_name}' subido correctamente a S3.")
except Exception as e:
    print("❌ Error subiendo el archivo a S3:", e)
    sys.exit(1)
