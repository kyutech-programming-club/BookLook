from backend import db

# モデル作成
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    cover = db.Column(db.String(80))


    def __init__(self, title, cover):
        self.title = title
        self.cover = cover

def register_book(title, cover):
    reg = Book(title, cover)
    db.session.add(reg)
    db.session.commit()
