from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Testing Secrets Manager for MWFeeds. This is a Demo Project."
    }
