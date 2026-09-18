from uuid import UUID

from sqlmodel import Session

from app.api.schemas import SourceRead, SourceWrite, NewsItemRead, PostRead, \
    TaskResponse, GeneratePayload


class SourceService:
    @staticmethod
    def list(session: Session) -> list[SourceRead]:
        return []

    @staticmethod
    def get(session: Session) -> SourceRead:
        return SourceRead(id=1)

    @staticmethod
    def create(session: Session, source: SourceWrite) -> SourceRead:
        return SourceRead(id=1)

    @staticmethod
    def update(cls, session, source_id, source):
        pass

    @staticmethod
    def delete(cls, session, source_id):
        pass


class NewsService:
    @staticmethod
    def list(session: Session) -> list[NewsItemRead]:
        return []


class PostService:
    @staticmethod
    def list(session: Session) -> list[PostRead]:
        return []


class TaskService:
    @staticmethod
    def parse(session: Session) -> TaskResponse:
        return TaskResponse(id=1)

    @staticmethod
    def generate(session: Session, payload: GeneratePayload) -> TaskResponse:
        return TaskResponse(id=2)

    @staticmethod
    def publish(session: Session, post_id: UUID) -> TaskResponse:
        return TaskResponse(id=3)
