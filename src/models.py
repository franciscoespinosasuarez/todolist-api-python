from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), unique=False, nullable=False)
    done = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<Todos %r>' % self.text

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "done": self.done
            # do not serialize the password, its a security breach
        }