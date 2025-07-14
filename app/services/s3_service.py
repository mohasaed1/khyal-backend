import os
import shutil
import uuid

UPLOAD_FOLDER = "uploads"

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def upload_file_to_s3(upload_file):
    """
    Save uploaded file locally in uploads/ and return relative URL.
    Replace later with actual S3 upload.
    """
    file_ext = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{file_ext}"
    save_path = os.path.join(UPLOAD_FOLDER, unique_filename)

    try:
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    except Exception as e:
        raise RuntimeError(f"Failed to save file locally: {str(e)}")

    # Return relative URL (served by FastAPI static)
    return f"/uploads/{unique_filename}"
