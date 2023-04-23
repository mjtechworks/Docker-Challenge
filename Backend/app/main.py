from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/test_users/{user_id}")
def get_user(user_id: str):
    

    user_id=user_id[::-1]
    return { "name": user_id }
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
