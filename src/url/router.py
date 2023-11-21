from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from fastapi import Depends, FastAPI, Request, APIRouter

from src.database import SessionLocal, engine
from src.url import models, schemas, service
from src.url.exceptions import raise_not_found

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


url_router = APIRouter(
    prefix="/url",
    tags=["shorter"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@url_router.post("/", response_model=schemas.URLInfo)
async def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    db_url = service.create_db_url(db=db, url=url)
    db_url.url = db_url.key
    return db_url


@url_router.get("/{url_key}")
async def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    if db_url := service.get_db_url_by_key(db=db, url_key=url_key):
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)
