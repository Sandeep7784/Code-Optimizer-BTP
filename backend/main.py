from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pathlib import Path
import sys
import uvicorn

UPLOAD_DIRECTORY = Path("data")
sys.path.append(str(Path(__file__).resolve().parent / "src"))
from src.root import main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)
#     file.filename = "input_code.c"  # Rename the uploaded file
#     file_path = UPLOAD_DIRECTORY / file.filename

#     with open(file_path, "wb") as f:
#         f.write(await file.read())

#     print("File saved to:", file_path)

#     return JSONResponse(content={"message": "File uploaded successfully.", "file_path": str(file_path)})

# @app.get("/results")
# async def process_file():
#     # Assuming the file to process is always 'input_code.c' in the upload directory
#     file_path = UPLOAD_DIRECTORY / "input_code.c"
    
#     # Check if the file exists before processing
#     if not file_path.exists():
#         return JSONResponse(status_code=404, content={"message": "File not found."})

#     # Call `main` function with the path to the saved file
#     result = main(file_path)
#     optimized_code = result[0]
#     explanation = result[1]
    
#     print("cool")
#     return JSONResponse(content={"optimizedCode": optimized_code, "explanation": explanation})

# @app.post("/upload") 
# async def upload_file(file: UploadFile = File(...)):
#     UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)
#     print(file.filename)    
#     file.filename = "input_code.c"
#     # print(len(file))   
#     file_path = UPLOAD_DIRECTORY / file.filename
#     with open(file_path, "wb") as f:
#         f.write(await file.read())

#     print("File saved to:", file_path)
#     # Call `main` function with the path to the saved file
#     # file_path  = "../"
#     parent_directory = file_path.parent.parent  # Get the parent directory of UPLOAD_DIRECTORY
#     print("Parent directory:", parent_directory)    

#     # res = []
#     # res.append()
#     result = main(file_path)
#     optimized_code = result[0]
#     explanation = result[1]
#     print("Optimized code:", type(optimized_code))
#     print("Explanation:", type(explanation))
#     return JSONResponse(content={"optimizedCode": optimized_code, "explanation": explanation})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    UPLOAD_DIRECTORY.mkdir(parents=True, exist_ok=True)
    file_path = UPLOAD_DIRECTORY / "input_code.c"
    
    try:
        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)
        
        print(f"File saved to: {file_path}")
        
        # Call main function
        result = main(file_path)
        optimized_code, explanation = result
        
        # Ensure types are correct
        if not isinstance(optimized_code, str):
            raise ValueError("Optimized code is not a string")
        if not isinstance(explanation, str):
            raise ValueError("Explanation is not a string")
        
        # print("Optimized code:", optimized_code[:100])
        # print("Explanation:", explanation[:100])
        return JSONResponse(
            content={"optimizedCode": optimized_code, "explanation": explanation},
            status_code=200
        )
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)

