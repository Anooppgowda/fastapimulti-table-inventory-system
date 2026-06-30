from fastapi import FastAPI
from routers import auth, product, order

app = FastAPI(
    title="E-Commerce & Inventory Management System",
    description="Multi-Table Database Management System API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(order.router)

@app.get("/")
def health_check():
    return {"status": "Online", "message": "System running securely."}