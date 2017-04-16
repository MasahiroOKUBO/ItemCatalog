import datetime
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.orm import relationship
from user import User
from category import Category
from ItemCatalog.utility import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    picture = Column(String(80))
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
        }
