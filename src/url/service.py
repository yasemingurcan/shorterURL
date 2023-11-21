from typing import Optional

from sqlalchemy.orm import Session

from src.url import models, schemas, keygen


def get_db_url_by_key(db: Session, url_key: str) -> Optional[models.URL]:
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key).first()
    )


def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    key = keygen.create_unique_random_key(db)
    secret_key = f"{key}_{keygen.create_random_key(length=8)}"
    db_url = models.URL(
        target_url=str(url.target_url), key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
