from fastapi import FastAPI

from dotenv import load_dotenv
import os


app = FastAPI()


load_dotenv()

TESTING_ENV_VARIABLE = os.getenv("TESTING_ENV_VARIABLE")


@app.get("/")
async def root():
    return {
        "message": "Testing Secrets Manager for MWFeeds. This is a Demo Project."
    }


@app.get("/test-access")
async def testing_env_variable():
    testing_variable = TESTING_ENV_VARIABLE or None
    return {
        "access_variable": testing_variable
    }
