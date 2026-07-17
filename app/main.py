"""
Webapp demo cho lab CI/CD.

API máy tính đơn giản gồm:
- Trang chủ
- Health check
- Cộng hai số
- Chia hai số
"""

from fastapi import FastAPI, HTTPException


# Khởi tạo ứng dụng FastAPI.
# title và version sẽ hiển thị trên trang Swagger UI.
app = FastAPI(
    title="CI/CD Demo App",
    version="1.0.0",
)


@app.get("/")
def read_root():
    """Trang chủ — trả về lời chào."""
    return {"message": "Hello DevOps! App đang chạy."}


@app.get("/health")
def health_check():
    """
    Health check endpoint.

    Docker, hệ thống giám sát hoặc load balancer có thể gọi endpoint
    này để kiểm tra ứng dụng còn hoạt động hay không.
    """
    return {"status": "ok"}


@app.get("/add")
def add(a: float, b: float):
    """
    Cộng hai số.

    Ví dụ:
    /add?a=1&b=2
    """
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.get("/divide")
def divide(a: float, b: float):
    """
    Chia hai số.

    Nếu b bằng 0, API trả về HTTP 400.
    """
    if b == 0:
        raise HTTPException(
            status_code=400,
            detail="Không thể chia cho 0",
        )

    return {
        "a": a,
        "b": b,
        "result": a / b,
    }