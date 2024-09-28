import os
from fastapi import FastAPI, Form, UploadFile, HTTPException
from fastapi.params import File
from tax_assistant.documents import process_document
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

import uuid

@app.post("/analyze-document")
async def analyze_document(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    try:
        # Generate a random UUID and prepend it to the filename
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        temp_file_path = f"./temp/{unique_filename}"
        os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)

        with open(temp_file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        logger.info(f"Received file: {unique_filename}")
        logger.info(f"Prompt: {prompt}")
        
        analysis = process_document(temp_file_path, prompt)
        
        if analysis:
            logger.info("Document analysis successful")
            return {"analysis": analysis}
        else:
            logger.error("Failed to analyze the document")
            raise HTTPException(status_code=500, detail="Failed to analyze the document")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)