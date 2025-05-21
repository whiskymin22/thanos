from fastapi import APIRouter, UploadFile, HTTPException
from app.services.process_excel import process_excel

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile):
    """
    Endpoint to upload and process an Excel file.
    """
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an Excel file.")

    # Process the uploaded file
    try:
        result = await process_excel(file)
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"message": "File processed successfully", "data": result}