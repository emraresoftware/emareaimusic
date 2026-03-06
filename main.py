# Emare AI Music — FastAPI Giriş Noktası

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.core.app:create_app",
        host="0.0.0.0",
        port=8700,
        reload=True,
        factory=True,
    )

# === Emare Feedback ===
from feedback_router import router as feedback_router
app.include_router(feedback_router, prefix="/api/feedback", tags=["feedback"])
# ======================

