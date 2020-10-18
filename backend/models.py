from backend import db

# モデル作成
class MyBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

def register_mybook(name):
    reg = MyBook(name)
    db.session.add(reg)
    db.session.commit()
