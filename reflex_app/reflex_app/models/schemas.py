import datetime
from typing import Optional

import sqlmodel


class User(sqlmodel.SQLModel, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    username: str = sqlmodel.Field(unique=True, index=True)
    password_hash: str
    created_at: datetime.datetime = sqlmodel.Field(
        default_factory=datetime.datetime.utcnow, nullable=False
    )

    __table_args__ = {"extend_existing": True}