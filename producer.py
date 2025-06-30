import boto3
import os
import sys

# Nombre del bucket como variable de entorno o por defecto
INPUT_BUCKET = os.getenv("INPUT_BUCKET", "upeu-producer-x-bucket-1")
FILE_PATH = sys.argv[1] if len(sys.argv) > 1 else ""

# Validaciones
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
    print(f"✅ Bucket '{INPUT_BUCKET}' existe.")
except s3.exceptions.ClientError:
    print(f"❌ Bucket '{INPUT_BUCKET}' no existe o no tienes acceso.")
    sys.exit(1)

# Subida del archivo
try:
    file_name = os.path.basename(FILE_PATH)
    s3.upload_file(FILE_PATH, INPUT_BUCKET, f"uploads/{file_name}")
    print(f"✅ Archivo '{file_name}' subido exitosamente a {INPUT_BUCKET}/uploads/")
except Exception as e:
    print(f"❌ Error al subir el archivo: {e}")
    sys.exit(1)
