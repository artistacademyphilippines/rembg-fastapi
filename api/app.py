from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
import base64
from io import BytesIO

app = FastAPI()

# Set up CORS middleware (equivalent to Flask-CORS)
origins = ["http://127.0.0.1:5503", "https://artistacademyphilippines.github.io"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins (you can restrict if needed)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def remove_background(request: Request):
    # Get the base64 string from the request body
    data = await request.body()

    return data
    '''
    # Decode the base64 string to image
    img_data = base64.b64decode(data.split(',')[1])
    
    # Process the image with rembg to remove the background
    removed_background = remove(img_data, post_process_mask=True)
    
    # Convert the result into a binary format
    new_data = BytesIO(removed_background)
    new_data.seek(0)

    # Convert binary to base64 format and decode again to text format
    new_base64 = base64.b64encode(new_data.getvalue()).decode('utf-8')

    # Return the base64 string directly (without wrapping it in JSON)
    return f"data:image/png;base64,{new_base64}"
    '''

# Run with Uvicorn in the terminal
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
