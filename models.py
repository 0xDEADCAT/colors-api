from config import db


# Class used by SQLAlchemy to build the Colors table in the database
class Color(db.Model):
    __tablename__ = 'Colors'

    color = db.Column(db.String(50), primary_key=True, nullable=False)
    value = db.Column(db.String(7), nullable=False)

    @property
    def serialize(self):
        return {
            'color': self.color,
            'value': self.value,
        }
