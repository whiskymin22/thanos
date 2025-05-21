from pydantic import BaseModel, FilePath

class UploadFileSchema(BaseModel):
    file: FilePath

    class Config:
        schema_extra = {
            "example": {
                "file": "path/to/your/excel/file.xlsx"
            }
        }