from fastapi import APIRouter, UploadFile, File, Form
from app.services.story_service import generate_story_text
from app.services.pdf_service import create_pdf
from app.services.s3_service import upload_file_to_s3

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok", "message": "Khyal.ai backend is running"}

@router.post("/generate-story")
def generate_story(child_name: str = Form(...)):
    """Generate a personalized story text"""
    story_text = generate_story_text(child_name)
    return {"child_name": child_name, "story": story_text}

@router.post("/generate-pdf")
def generate_pdf(child_name: str = Form(...), story_text: str = Form(...)):
    """Generate a PDF from the story"""
    pdf_path = create_pdf(child_name, story_text)
    return {"pdf_url": pdf_path}

@router.post("/upload-photo")
def upload_photo(file: UploadFile = File(...)):
    """Upload a photo to S3/local storage"""
    file_url = upload_file_to_s3(file)
    return {"file_url": file_url}
