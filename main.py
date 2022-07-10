from fastapi import FastAPI

from routers import items, auth

app = FastAPI()

# Routers
app.include_router(items.router, prefix="/items", tags=["items (protected)"])
app.include_router(auth.router, tags=["auth"])


@app.get("/healthcheck")
def health_check():
    return {"msg": "OK"}
