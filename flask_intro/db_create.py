# import db from app: db is a SQLAlchemy object.
from app import db
# import database Schema.
from models import BlogPost

# create a database and db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

# commit
db.session.commit()