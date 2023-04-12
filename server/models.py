from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('phone')
    def validates_phone(self, key, value):
        if len(value) != 10:
            raise ValueError("Please enter a valid phone number")
        return value
    @validates('name')
    def validates_name(self, key, value):
        names = db.session.query(Author.name).all()
        if not value:
            raise ValueError("Please enter your name")
        elif value in names:
            raise ValueError("Please enter a unique name")
        return value
            

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    
@validates('title')
def validates_title(self, key, value):
    if not value:
        raise ValueError('Please enter a title')
    return value

@validates('content', 'summary')
def validates_content(self, key, value):
    if len(value) < 250:
        raise ValueError("Content must be at least 250 characters long")
    if (key == 'summary'):
        if len(value) > 250:
            raise ValueError("Summary must be less than 250 characters")
    return value

@validates('category')
def validate_category(self, key, category):
    if category != 'Fiction' and category != 'Non-Fiction':
        raise ValueError("Category must be Fiction or Non-Fiction.")
    return category

    
