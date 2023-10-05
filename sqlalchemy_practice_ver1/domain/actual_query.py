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
#     filter_by(name='some user').one()
#     return _oneuser_name

# def get_firstuser_name(db: Session):
#     _firstuser_name = db.query(User).\
#     filter_by(name='some user').first()
#     return _firstuser_name



# 5. joinedload
def get_user_address(db: Session):
    _user_address = db.query(User).options(
    joinedload(User.address) # innerjoin=True
    ).all()
    return _user_address


# 6. join + filter
def get_address_sameemail(db: Session):
    _address_sameemail = db.query(User).\
    join(Address).\
    filter(Address.email == 'e@sa.us').\
    all()
    return _address_sameemail


# 7. from_statement
def get_user_selectfrom(db: Session):
    _user_selectfrom = db.query(User).\
    from_statement(
    text("select * from user")
    ).all()
    return _user_selectfrom






# 8. contains_eager + populate_existing
def get_user_address_join(db: Session):
    _user_address_join = db.query(User).\
    join(User.address).\
    options(contains_eager(User.address)).\
    populate_existing().all()
    return _user_address_join

# 8.1 populate_existing_test
def get_user_address_join_2(db: Session):
    _user_info = db.query(User).\
    join(User.address).\
    filter(Address.email.like("%@rbrain.co.kr")).\
    options(contains_eager(User.address)).\
    all() # populate_existing().
    return _user_info


# 9. update + synchronize_Session="evaluate"
def put_foo2foobar(db: Session):
    _foo2foobar = db.query(User).\
    filter(User.name == 'foo').\
    update(
        {"fullname": "Foo Bar"},
        synchronize_session="evaluate"
    )
    # db.commit()
    return _foo2foobar


# 10. count
def get_user_count(db: Session):
    _user_count = db.query(User).count()
    return _user_count
