from app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp())


class SentimentRequest(Base):

    __tablename__ = 'sentiment_requests'

    keyword = db.Column(db.String(128), nullable=False)
    by_user_email = db.Column(db.String(128), nullable=False)

    def __init__(self, keyword, by_user_email, password):

        self.keyword = keyword
        self.by_user_email = by_user_email

    def __repr__(self):
        return '<User %r>' % (self.keyword)
