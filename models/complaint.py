from init import db, ma
from marshmallow import fields

# SQLAlchemy: Complaint Details
class Complaint(db.Model):
    __tablename__= 'complaints'

    id          = db.Column(db.Integer, primary_key=True)
    subject     = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    entry_time  = db.Column(db.Date)
    # Foreign Keys
    profile_id  = db.Column(db.Integer, db.ForeignKey('profiles.id'), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    # Foreign Key Relationships
    profile     = db.relationship('Profile', back_populates='complaints', cascade ='all, delete')
    employee    = db.relationship('Employee', back_populates='complaints', cascade ='all, delete')

# Marshmallow: Complaint Schema
class ComplaintSchema(ma.Schema):
    # Nested Attributes
    profile    = fields.List(fields.Nested('ProfileSchema'))
    employee   = fields.List(fields.Nested('EmployeeSchema'), exclude=['password','employee'])

    class Meta:
        fields  = ('id', 'subject', 'description', 'entry_time', 'profile', 'employee')
        ordered = True