from app import db
from models import Pet

db.drop_all()
db.create_all()

p = Pet(name="Shiro", species="Cat - American short hair", photo_url="https://images.unsplash.com/photo-1595229497219-b1b5a2e56002?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80", age=2, notes="Shiro loves to play!", available=True)

db.session.add(p)
db.session.commit()