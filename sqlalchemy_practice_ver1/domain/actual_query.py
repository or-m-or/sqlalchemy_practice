from models import User, Address
from sqlalchemy.orm import Session, joinedload, contains_eager
from sqlalchemy import text



# def get_user_id42(db: Session):
#     _user_id42 = db.query(User).get(42)
#     return _user_id42

# def get_user_all(db: Session):
#     _user_all = db.query(User).all()
#     return _user_all

# def get_oneuser_name(db: Session):
#     _oneuser_name = db.query(User).\
#     filter_by(name='sample1').one()
#     return _oneuser_name

# def get_firstuser_name(db: Session):
#     _firstuser_name = db.query(User).\
#     filter_by(name='some user').first()
#     return _firstuser_name


# 6. join + filter
def get_join_test(db: Session):
    _get_join_test = db.query(User).\
    join(Address).all()
    #filter(Address.email.like('%@rbrain.co.kr'))
    #all() # filter(Address.email.like('%@gmail.com')).\
    return _get_join_test

# 5. joinedload
def get_joinedload_test(db: Session):
    _get_joinedload_test = db.query(User).options(joinedload(User.address)).\
    filter(Address.email.like('%@rbrain.co.kr')).\
    all() # filter(Address.email.like('%@rbrain.co.kr')).\
    # join(Address). -> 조인 중복, filter 기능동작함
    return _get_joinedload_test

# 8.1 contains_eager + populate_existing
def get_contains_eager_test(db: Session):
    _get_contains_eager_test = db.query(User).\
    join(User.address).\
    options(contains_eager(User.address)).\
    populate_existing().\
    all()
    # filter(Address.email.like("%@rbrain.co.kr")).\
    return _get_contains_eager_test


# 8.2 populate_existing_test
def add_address(db: Session):
    new_address = Address(id=11, email='test5@gmail.com', user_id=5)
    db.add(new_address)
    db.commit()

def get_populate_existing_test(db: Session):
    query1 = db.query(User).join(User.address).options(contains_eager(User.address)).all()

    # db업데이트 : user5에 해당하는 address값 추가
    # add_address(db)

    return query1


# 9. update + synchronize_Session="evaluate"
def put_synchronize_Session_test(db: Session):
    _put_synchronize_Session_test = db.query(User).\
    filter(User.name == 'foo').\
    update(
        {"fullname": "Foo Bar"},
        synchronize_session="evaluate"
    )
    # db.commit()
    return _put_synchronize_Session_test

# 7. from_statement
def get_from_statement_test(db: Session):
    _get_from_statement_test = db.query(User).\
    from_statement(
    text("select * from user")
    ).all()
    return _get_from_statement_test

# 10. count
def get_count_test(db: Session):
    _get_count_test = db.query(User).count()
    return _get_count_test
