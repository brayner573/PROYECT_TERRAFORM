import boto3
import os
import sys

INPUT_BUCKET = os.getenv("INPUT_BUCKET", "upeu-producer-x-bucket-1")
FILE_PATH = sys.argv[1] if len(sys.argv) > 1 else None

if not FILE_PATH:
    print("❌ Debes proporcionar el path del archivo .csv")
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
    print(f"❌ Bucket '{INPUT_BUCKET}' no encontrado.")
    sys.exit(1)

# Sube el archivo CSV
key = f"uploads/{os.path.basename(FILE_PATH)}"
s3.upload_file(FILE_PATH, INPUT_BUCKET, key)
print(f"✅ Archivo '{FILE_PATH}' subido como '{key}' a '{INPUT_BUCKET}'")
