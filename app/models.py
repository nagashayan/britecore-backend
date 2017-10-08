from app import db

class FeatureDetails(db.Model):
    """This class represents the FeatureDetailsetlist table."""

    __tablename__ = 'featuredetails'

    client_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    target_date = db.Column(db.DateTime)
    product_area = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    def __init__(self, client_id, title, description, target_date, product_area):
        """initialize with name."""
        self.client_id = client_id
        self.title = title
        self.description = description
        self.target_date = target_date
        self.product_area = product_area

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return FeatureDetails.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<FeatureDetails: {}>".format(self.title)