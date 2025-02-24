from pydantic import BaseModel


# ###
# class ArticleBaseSchema(BaseModel):
#     title: str
#     content: str
#     author_id: int
#     tag_id: int
#     category_id: int
#
#
#     class Config:
#         from_attributes = True
#
#
# class ArticleCreateSchema(ArticleBaseSchema):
#     pass
#
#
# class ArticleSchema(ArticleBaseSchema):
#     id: int
