from fastapi import FastAPI, Depends, Request
from fastapi import FastAPI, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

from auth import verify_api_key
from services.data_collector import get_sector_news
from services.ai_analyzer import analyze_sector_with_ai
from utils.markdown_builder import build_markdown_report

app = FastAPI()

limiter = Limiter(key_func=get_remote_address)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"message": "Too many requests"}
    )

@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
def analyze_sector(request: Request, sector: str, auth=Depends(verify_api_key)):

    news = get_sector_news(sector)

    analysis = analyze_sector_with_ai(sector, news)

    report = build_markdown_report(sector, news, analysis)

    return {
        "sector": sector,
        "report": report
    }