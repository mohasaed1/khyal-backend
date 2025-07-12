import os
from fastapi import UploadFile

def upload_file_to_s3(file: UploadFile) -> str:
    # MVP: Save locally (replace with S3 upload later)
    save_path = f"static/{file.filename}"
    with open(save_path, "wb") as buffer:
        buffer.write(file.file.read())
    return save_path
