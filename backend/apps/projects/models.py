from datetime import datetime
from database import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    imageUrl = db.Column(db.String(100), nullable=False)
    contractTypeId = db.Column(db.Integer, nullable=False)
    contractSignedOn = db.Column(db.DateTime, nullable=False, default = datetime.now())
    budget = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, nullable=False)