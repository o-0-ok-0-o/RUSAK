# from fastapi import APIRouter, Depends, HTTPException
# from typing import Annotated
#
# from sqlalchemy import select
# from src.db.database import get_async_session
# from sqlalchemy.ext.asyncio import AsyncSession

#
# router = APIRouter(prefix="/article", tags=["Посты"])
#
#
# @router.post("", summary="Создание поста")
# async def create_article(
#     article: Annotated[ArticleCreateSchema, Depends()],
#     session: AsyncSession = Depends(get_async_session),
# ):
#     article_dict = article.model_dump()
#
#     article_model = Article(**article_dict)
#     session.add(article_model)
#     await session.commit()
#
#     return {"success": True, "article": article}
#
#
# @router.get("", response_model=list[ArticleSchema], summary="Получение всех постов")
# async def get_all_articles(session: AsyncSession = Depends(get_async_session)):
#     articles = await session.execute(select(Article))
#     return articles.scalars().all()
#
#
# @router.get(
#     "/{article_id}", response_model=ArticleSchema, summary="Получение одного поста"
# )
# async def get_article(
#     article_id: int, session: AsyncSession = Depends(get_async_session)
# ):
#     article = await session.get(Article, article_id)
#
#     if not article:
#         raise HTTPException(status_code=404, detail="Тег не найден")
#     return article
#
#
# @router.patch(
#     "/{article_id}", response_model=ArticleBaseSchema, summary="Изменение поста"
# )
# async def update_article_name(
#     article_id: int,
#     article_update: ArticleBaseSchema,
#     session: AsyncSession = Depends(get_async_session),
# ):
#     article = await session.get(Article, article_id)
#
#     if article == None:
#         raise HTTPException(status_code=404, detail="Пост не найден")
#
#     article_data = article_update.model_dump(exclude_unset=True)
#     for key, value in article_data.items():
#         setattr(article, key, value)
#
#     await session.commit()
#     await session.refresh(article)
#     return {"new_article_set": True, "article": article}
#
#
# @router.delete("/{article_id}", summary="Удаление поста")
# async def delete_article(
#     article_id: int, session: AsyncSession = Depends(get_async_session)
# ):
#     article = await session.get(Article, article_id)
#
#     if article == None:
#         raise HTTPException(status_code=404, detail="Пост не найден")
#     await session.delete(article)
#     await session.commit()
#     return {"succes_delete": True}
