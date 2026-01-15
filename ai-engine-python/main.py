from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "online", 
        "message": "Blip Docs Assistant AI Engine is running!",
        "version": "1.0.0",
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}