from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow your frontend to access the FastAPI app
origins = ["http://127.0.0.1:5503", "https://artistacademyphilippines.github.io"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows these origins to make requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post('/')
async def index(request: Request):
    data = await request.body()
    print(data)
    
'''
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
import base64
from io import BytesIO

# Create FastAPI app
app = FastAPI()

# Add CORS middleware to allow your frontend to access the FastAPI app
origins = ["http://127.0.0.1:5503", "https://artistacademyphilippines.github.io"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows these origins to make requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# The POST endpoint for background removal
@app.post("/", response_class=HTMLResponse)
async def remove_background(request: Request):
    # Get the base64 string from the request body
    data = await request.body()

    # Decode the base64 string to image
    img_data = base64.b64decode(data.split(b',')[1])

    # Process the image with rembg to remove the background
    removed_background = remove(img_data, post_process_mask=True)

    # Convert the result into a binary format
    new_data = BytesIO(removed_background)
    new_data.seek(0)

    # Convert binary to base64 format and decode again to text format
    new_base64 = base64.b64encode(new_data.getvalue()).decode('utf-8')

    # Return the base64 string directly as HTML response (image data)
    return f"data:image/png;base64,{new_base64}"
'''
