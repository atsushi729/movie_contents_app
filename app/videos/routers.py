from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request

from app.shortcuts import render

router = APIRouter(
    prefix='/videos'
)


@router.get("/", response_class=HTMLResponse)
def video_list_view(request: Request):
    return render(request, "videos/list.html", {})


@router.get("/detail", response_class=HTMLResponse)
def video_list_view(request: Request):
    return render(request, "videos/detail.html", {})