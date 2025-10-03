from flask import request
from flask_restful import Resource
from db import db
from models import Contact
from schema import ContactSchema

def error(msg: str, code: int = 404, key: str = "error"):
    return {key: msg, "code": code}, code


def ok(result: str, code: int = 200):
    return result, code


class Contacts(Resource):
    def get(self):
        Contacts_schema = ContactSchema(many=True)
        return Contacts_schema.dump(Contact.query.all())

    def post(self):
        Contact = Contact(
            id=None,
            name=request.json['name'],
            email=request.json['email']
        )
        db.session.add(Contact)
        db.session.commit()

        return ok(ContactSchema().dump(Contact))


class ContactResource(Resource):
    def get(self, contact_id):
        Contact = Contact.query.get(contact_id)
        if Contact is None:
            return error(f"Contact id {contact_id} not found")

        return ok(ContactSchema().dump(Contact))

    def delete(self, contact_id):
        Contact = Contact.query.get(contact_id)
        if Contact is None:
            return error(f"Contact id {contact_id} not found")
        db.session.delete(Contact)
        db.session.commit()
        return {"message": f"deleted Contact {Contact.name}"}, 201


def register_apis(api):
    api.add_resource(Contacts, "/contacts")
    api.add_resource(ContactResource, "/contact/<contact_id>")
