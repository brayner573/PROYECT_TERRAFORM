import boto3
import os
import sys

INPUT_BUCKET = os.getenv("INPUT_BUCKET", "upeu-producer-x-bucket-1")
FILE_PATH = sys.argv[1] if len(sys.argv) > 1 else ""

if not FILE_PATH:
    print("❌ Debes proporcionar el path del archivo .csv")
    sys.exit(1)

if not FILE_PATH.endswith('.csv'):
    print("❌ Solo se permiten archivos .csv")
    sys.exit(1)

s3 = boto3.client("s3")

try:
    s3.head_bucket(Bucket=INPUT_BUCKET)
    print(f"✅ Bucket '{INPUT_BUCKET}' verificado.")
except s3.exceptions.ClientError:
    print(f"❌ Bucket '{INPUT_BUCKET}' no existe o no es accesible.")
    sys.exit(1)

try:
    filename = os.path.basename(FILE_PATH)
    s3.upload_file(FILE_PATH, INPUT_BUCKET, f"uploads/{filename}")
    print(f"✅ Archivo '{filename}' subido exitosamente al bucket '{INPUT_BUCKET}/uploads/'.")
except Exception as e:
    print(f"❌ Error al subir archivo: {str(e)}")
    sys.exit(1)
