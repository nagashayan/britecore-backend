from . import db
from sqlalchemy import CheckConstraint, UniqueConstraint, text

class FeatureDetails(db.Model):
    """This class represents the FeatureDetailsetlist table."""

    __tablename__ = 'featuredetails'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer,  CheckConstraint('client_id>0'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    target_date = db.Column(db.DateTime, nullable=False)
    product_area = db.Column(db.String(255), nullable=False)
    client_priority = db.Column(db.Integer, CheckConstraint('client_priority>0'))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    #add unique constraint
    __table_args__ = (UniqueConstraint('client_id', 'client_priority', name='u_cons1'),)

    def checkPriorityOrder(self):
        
        features = FeatureDetails.query.filter(FeatureDetails.client_id==self.client_id).filter( FeatureDetails.client_priority >= self.client_priority).order_by(FeatureDetails.client_priority).all()
        foundsame = False
        
        if len(features) > 0:
            
            if features[0].client_priority == int(self.client_priority):
                foundsame = True
            

        if foundsame:
            if features is not None:
                prevpriority = None
                for feature in features:
                    
                    if prevpriority is None:
                        prevpriority = feature.client_priority
                    
                    if prevpriority == feature.client_priority:
                        feature.client_priority += 1
                        db.session.add(feature)
                
                        
                        prevpriority = feature.client_priority
                db.session.commit()
            

    def __init__(self, client_id, title, description, target_date, product_area, client_priority):
        """initialize"""
        self.client_id = client_id
        self.client_priority = client_priority
        self.title = title
        self.description = description
        self.target_date = target_date
        self.product_area = product_area

        
        #self.checkPriorityOrder()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return FeatureDetails.query.order_by(FeatureDetails.client_id,FeatureDetails.client_priority).all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def upgrade():
        db.create_unique_constraint('client_id', 'client_priority', ['name','u_cons1'])

    