import datetime

from database import db
from marshmallow_sqlalchemy import ModelSchema

class Members(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime,
                            onupdate=datetime.datetime.now,
                            default=datetime.datetime.now)

    def create(self, member):
        success = True
        try:
            new_members = Members(
                    username = member['username'],
                    email = member['email'],
                    password = member['password'])

            db.session.add(new_members)
            db.session.commit()
            return new_members.id
        except:
            db.session.rollback()
            success = False
            raise
        finally:
            db.session.close()

        return success

    def delete(self, ID):
        success = True
        try:
            member = Members.query.get(ID)
            if member is not None:
                db.session.delete(member)
                db.session.commit()
        except:
            db.session.rollback()
            success = False
            raise
        finally:
            db.session.close()

        return success

    def update(self, member):
        success = True
        try:
            filterMember = Members.query.get(member['id'])

            filterMember.username = member['username']
            filterMember.email = member['email']
            filterMember.password = member['password']
            db.session.commit()
        except:
            db.session.rollback()
            success = False
            raise
        finally:
            db.session.close()

        return success

class MembersSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ('id', 'username', 'email', 'password', 'create_time', 'update_time')

members_schema = MembersSchema()
members_schema = MembersSchema(many=True)