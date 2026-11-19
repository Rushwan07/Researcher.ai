from fastapi import FastAPI


app = FastAPI(
    title="Researcher.ai",
    description="Intelligent Knowledge and Research Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message":"Application is ruuning home",
        "status":"success!!"
    }
    
@app.get("/docs")
def docs():
    return {
        "message":"Application is ruuning docs",
        "status":"success!!"
    }