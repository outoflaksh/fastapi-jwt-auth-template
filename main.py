from fastapi import FastAPI

from routers import items, auth

app = FastAPI()

# Routers
app.include_router(items.router, prefix="/items")
app.include_router(auth.router)


@app.get("/healthcheck")
def health_check():
    return {"msg": "OK"}
