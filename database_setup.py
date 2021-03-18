from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Class used by SQLAlchemy to build the Colors table in the database
class Color(Base):
    __tablename__ = 'Colors'

    color = Column(String(50), primary_key=True)
    value = Column(String(4), nullable=False)


engine = create_engine('sqlite:///colors.db')

Base.metadata.create_all(engine)
