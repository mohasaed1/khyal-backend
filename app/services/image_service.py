import os
import shutil
import uuid

UPLOAD_FOLDER = "uploads"

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_uploaded_image(upload_file):
    """
    Save uploaded image to the uploads folder and return its relative path.
    """
    file_ext = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{file_ext}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    except Exception as e:
        raise RuntimeError(f"Failed to save image: {str(e)}")

    return f"/{UPLOAD_FOLDER}/{unique_filename}"
