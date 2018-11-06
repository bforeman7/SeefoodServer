from server import database

class ImageModel(database.Model):
    
    __tablename__ = 'images'

    ## images table columns / imageModel object attributes
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80))
    date_taken = database.Column(database.DateTime)
    first_class_confidence = database.Column(database.Float)
    second_class_confidence = database.Column(database.Float)
    image_path = database.Column(database.String)

    def __init__(self, name, date_taken, first_class_confidence, second_class_confidence, image_path):
        self.name=name
        self.date_taken=date_taken
        self.first_class_confidence=first_class_confidence
        self.second_class_confidence=second_class_confidence
        self.image_path=image_path

    #query db by id
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    #json representation of db data
    def json(self):
        return {
            'id': self.id,
            'date_taken': self.date_taken,
            'first_class_confidence': self.first_class_confidence,
            'second_class_confidence': self.second_class_confidence,
            'image_path': self.image_path
        }

    def save_to_database(self):
        database.session.add(self)
        database.session.commit()

    def delete_from_database(self):
        database.session.delete(self)
        database.session.commit()
