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

    # Add validators 
    @validates('name')
    def validates_name(self, key, user_name):
        if not user_name:
            raise ValueError("You must enter a name!!")
        elif user_name in [user.name for user in Author.query.all()]:
            raise ValueError("Name must be unique")
        return user_name
    
    @validates('phone_number')
    def validates_phone_number(self, key, phone_number):
        cln_phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(cln_phone_number) != 10:
            raise ValueError("Number must be 10")
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('title')
    def validates_title(self, key, title):
        click_baits = ["Won't Believe", "Secret", "Top", "Guesscl"]
        if not title:
            raise ValueError("You must enter a title!!")
        # for bait in click_baits:
        #     if bait not in title:
        #         raise ValueError("You must enter a title with clickbaits!!")
        return title
    
    @validates('content')
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Length must be at least 250")
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError("Summary must be at least 250")
        return summary
    
    @validates('category')
    def validate_category(self, key, category):
        if category!='Fiction' and category!='Non-Fiction':
            raise ValueError("Category: Fiction or Non-Fiction")
        return category

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
