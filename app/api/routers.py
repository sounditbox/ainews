from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.api.schemas import SourceRead, SourceWrite, SourceUpdate, NewsItemRead, \
    PostRead, TaskResponse
from app.db import get_session
from app.models import SourceType

router = APIRouter(
    prefix="/api",
    tags=["v1"],
    responses={404: {"description": "Not found"}}
)

SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/sources", response_model=list[SourceRead])
async def list_sources(session: SessionDep):
    return []


@router.get("/sources/{source_id}", response_model=SourceRead,
            responses={404: {"description": "Not found"}})
async def get_source(source_id: int, session: SessionDep):
    return SourceRead(
        id=source_id,
        type=SourceType.SITE,
        name="Test",
        url="https://example.com", enabled=True
    )


@router.post("/sources", response_model=SourceWrite,
             status_code=201, responses={400: {"description": "Invalid data"}})
async def create_source(source: SourceWrite, session: SessionDep):
    return source


@router.patch("/sources/{source_id}", response_model=SourceUpdate,
              responses={404: {"description": "Not found"}})
async def update_source(source_id: UUID, source: SourceUpdate,
                        session: SessionDep):
    return source


@router.delete("/sources/{source_id}", status_code=204,
               responses={404: {"description": "Not found"}}
               )
async def delete_source(source_id: int):
    pass


@router.get("/news", response_model=list[NewsItemRead])
async def list_news(session: SessionDep):
    return []


@router.get("/posts", response_model=list[PostRead])
async def list_posts(session: SessionDep):
    return []


@router.post("/parse", response_model=TaskResponse)
async def parse_sources_enpoint():
    return TaskResponse(id=1)


@router.post("/generate", response_model=TaskResponse)
async def generate_post_enpoint():
    return TaskResponse(id=2)


@router.post("/posts/{id}/publish", response_model=TaskResponse)
async def publish_post_endpoint():
    return TaskResponse(id=3)

