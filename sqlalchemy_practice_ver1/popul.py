# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('sqlite:///:memory:')
# Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()

# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     address = None  # 주소 정보는 초기에 None으로 설정

# Base.metadata.create_all(engine)

# # 사용자 정보 추가
# user = User(name="John")
# session.add(user)
# session.commit()

# # 사용자 정보 로드
# loaded_user = session.query(User).first()

# # 주소 정보는 아직 로드하지 않았으므로 None
# print("Loaded User Name:", loaded_user.name)  # 출력: Loaded User Name: John
# print("Loaded User Address:", loaded_user.address)  # 출력: Loaded User Address: None

# # 사용자 이름 변경
# loaded_user.name = "Alice"
# session.commit()

# # 다시 로드한 사용자 정보
# loaded_user = session.query(User).first()

# # 주소 정보는 여전히 None
# print("Updated User Name:", loaded_user.name)  # 출력: Updated User Name: Alice
# print("Updated User Address:", loaded_user.address)  # 출력: Updated User Address: None

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = None  # 주소 정보는 초기에 None으로 설정

Base.metadata.create_all(engine)

# 사용자 정보 추가
user = User(name="John")
session.add(user)
session.commit()

# 사용자 정보 로드
loaded_user = session.query(User).first()

# 주소 정보는 아직 로드하지 않았으므로 None
print("Loaded User Name:", loaded_user.name)  # 출력: Loaded User Name: John
print("Loaded User Address:", loaded_user.address)  # 출력: Loaded User Address: None

# 사용자 이름 변경
loaded_user.name = "Alice"
session.commit()

# 다시 로드한 사용자 정보
loaded_user = session.query(User).first()

# 주소 정보 업데이트 시뮬레이션
new_address = "123 Main St."
loaded_user.address = new_address

# populate_existing()를 사용하여 주소 정보 업데이트
session.add(loaded_user)
session.flush()
session.refresh(loaded_user)

# 업데이트된 주소 정보 확인
print("Updated User Name:", loaded_user.name)  # 출력: Updated User Name: Alice
print("Updated User Address:", loaded_user.address)  # 출력: Updated User Address: 123 Main St.
