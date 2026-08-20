from models import Contact
from marsh import ma


class ContactSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Contact

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    subject = ma.auto_field()
    message = ma.auto_field()
