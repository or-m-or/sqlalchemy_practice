from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    address = relationship('Address', back_populates='user') 
    # 부모 객체 값이 변할 때 자식 객체의 연관된 속성도 동기화
    # back_populates 는 부모,자식 테이블에 모두 지정해야 함
    # backref 는 부모 테이블에만 지정하면 됨

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))  # 자식 테이블이 부모 테이블을 외래키로 참조
    user = relationship('User', back_populates='address') 