from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from db.models.base import Base


class ExampleModel(Base):
    __tablename__ = "example_model"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
