from models import User, Address
from sqlalchemy.orm import Session, joinedload, contains_eager
from sqlalchemy import text


# # test query
# def get_user_list(db: Session):
#     _user_list = db.query(User)\
#     .order_by(User.id.desc())\
#     .all()
#     return _user_list

# 1. User 테이블에서 ID가 42인 사용자를 가져와서, 해당 사용자 객체를 반환
def get_user_id42(db: Session):
    _user_id42 = db.query(User).get(42)
    return _user_id42


# 2. User 테이블의 모든 레코드를 가져와서 리스트로 반환
def get_user_all(db: Session):
    _user_all = db.query(User).all()
    return _user_all


# 3. User 테이블에서 'name'='some user'인 단일 사용자 레코드를 가져와서 반환 
#    'name'='some user'인 레코드가 하나가 아닐 경우, 같은 이름이 둘이면 에러 발생함. (sqlalchemy.exc.MultipleResultsFound: Multiple rows were found when exactly one was required)
def get_oneuser_name(db: Session):
    _oneuser_name = db.query(User).\
    filter_by(name='some user').one()
    return _oneuser_name


# 4. User 테이블에서 'name'='some user'인 첫 번째 사용자 레코드를 가져와서 반환하며, 결과가 없으면 None을 반환.
def get_firstuser_name(db: Session):
    _firstuser_name = db.query(User).\
    filter_by(name='some user').first()
    return _firstuser_name


# 5. User 테이블의 모든 레코드를 가져오면서 각 User 레코드와 관련된 addresses 속성을 미리 로드하여 리스트로 반환
# joinedload : Eager Loading의 한 형태로, 필요한 데이터를 미리 로드하여 N+1 쿼리 문제를 해결하고 성능을 최적화
#              어떤 테이블에서 특정 정보를 검색한 후에, 연관된 다른 테이블의 데이터도 가져오려고 할 때 사용.
#              joinedLoad를 사용하지 않는 경우, 테이블을 검색하는 쿼리가 한 번 실행되고, 그 다음 다른 테이블에서 각 데이터와 연관된 데이터를 가져오기 위한 추가 쿼리가 N번 실행됨. 
#              -> 성능 저하
#              연관된 데이터를 한 번의 쿼리로 가졀 수 있게, 연관 테이블 데이터를 미리 로드하여 가져옴

# join : SQL 조인과 유사한 개념으로 두 개 이상의 테이블을 연결하여 하나의 테이블로 결합하는 것을 의미
def get_user_address(db: Session):
    _user_address = db.query(User).options(
    joinedload(User.address)
    ).all()
    return _user_address


# 6. User와 Address 테이블을 조인하고, Address 테이블의 이메일 주소가 'e@sa.us'인 사용자 정보를 검색
#    filter : 필터링 조건을 정의
def get_address_sameemail(db: Session):
    _address_sameemail = db.query(User).\
    join(Address).\
    filter(Address.email == 'e@sa.us').\
    all()
    return _address_sameemail

# 7. 데이터베이스에서 "select * from users" SQL 쿼리를 실행하여 모든 User 레코드를 가져와서 리스트로 반환
# SQL쿼리 문 실행
def get_user_selectfrom(db: Session):
    _user_selectfrom = db.query(User).\
    from_statement(
    text("select * from user")
    ).all()
    return _user_selectfrom


# 8. 데이터베이스에서 User와 관련된 Address 레코드를 조인하고, 
# User 객체에 연결된 address 관계를 미리 로드하여 
# 이미 로드된 데이터를 사용하여 모든 User 레코드를 가져와서 리스트로 반환
"""
join 으로 User테이블과 Address테이블 조인
Eager loading을 사용하여 User테이블과 연결된 Address 데이터를 세션에 미리 로드
populate_existing : 이미 세션에 로드된 객체(Address)에 User테이블의 데이터를 다시 로드하여 업데이트
"""


def get_user_address_join(db: Session):
    _user_address_join = db.query(User).\
    join(User.address).\
    options(
    contains_eager(User.address)
    ).\
    populate_existing().all()
    return _user_address_join


# X joinedload = contains_eager + join
# contains_eager = USER객체를 만들때 조인된 Address값 채워주려면 명시

# 

# 9. 데이터베이스에서 name이 'foo'인 모든 User 레코드의 fullname을 "Foo Bar"로 업데이트하고, 세션의 상태를 업데이트
"""
synchronize_session="evaluate" 옵션은 세션 내부 상태를 업데이트하는 방식을 지정하는 것으로, 
"evaluate" 옵션은 세션 내부 상태를 업데이트하지만 데이터베이스에는 아직 커밋하지 않음을 의미함.
즉, 이 쿼리문은 User 테이블에서 name이 'foo'인 레코드의 fullname 값을 "Foo Bar"로 변경하는 작업을 수행하며, 
이 변경 사항은 세션 내부에 적용되고, 나중에 커밋할 수 있도록 준비됩니다. 커밋을 수행하면 데이터베이스에 변경 사항이 적용됨.
"""
def put_foo2foobar(db: Session):
    _foo2foobar = db.query(User).\
    filter(User.name == 'foo').\
    update(
        {"fullname": "Foo Bar"},
        synchronize_session="evaluate"
    )
    # db.commit()
    return _foo2foobar


# 10. 데이터베이스에서 User 테이블의 레코드(튜플, 행)의 개수를 가져와서 반환
"""
방법 1

- **`select(func.count())`**는 레코드 수를 계산하는 서브쿼리를 생성
- **`select_from(User)`**는 이 서브쿼리를 User 테이블에서 실행하도록 지정
- 최종 SQL 쿼리는 "SELECT count(*) FROM User"와 같이 레코드 수를 계산

방법 2

- 이 방법은 테이블의 특정 열을 직접 사용하여 레코드 수를 계산
- **`select(func.count(User.id))`**는 User 테이블의 "id" 열의 값을 사용하여 레코드 수를 계산하는 SQL 쿼리를 생성
- 최종 SQL 쿼리는 "SELECT count(User.id) FROM User"와 같이 레코드 수를 계산
"""
def get_user_count(db: Session):
    _user_count = db.query(User).count()
    return _user_count
