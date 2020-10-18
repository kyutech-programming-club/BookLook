from backend import db

# モデル作成
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    cover = db.Column(db.String(80))


    def __init__(self, title, cover):
        self.title = title
        self.cover = cover

    def to_dict(self):
        return dict(
            title = self.title,
            cover = self.cover
        )

def register_book(title, cover):
    reg = Book(title, cover)
    db.session.add(reg)
    db.session.commit()

def get_all():
    books = db.session.query(Book).all()
    return books
