from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import Session


sqlite_file_name = "rusak.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(
    sqlite_url,
    connect_args=connect_args,
    echo=True,
)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
# async_engine = create_async_engine(sqlite_file_name)
# async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)
#
#
# async def get_async_session():
#     async with async_session_factory() as session:
#         yield session

