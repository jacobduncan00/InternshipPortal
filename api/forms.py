# Internship Portal Web App
# forms.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the forms.py file, this will change later.
"""

from flask import Blueprint, request

from .models import db, ClientsModel, ListingsModel, UsersModel
import hashlib  # Using for password hashing (SHA-256)

# Create auth blueprint:
forms = Blueprint('forms', __name__)


# Route for submitting forms:
@forms.route('/contact-submit', methods=['POST'])
def contact_submit():
    """Contact submission route.
    This function handles the contact submissions.
    """
    data = request.json
    name = data['name']
    email = data['email']
    message = data['message']
    print(f'Name: {name}, Email: {email}, Message: {message}')
    response = {'status': 200}

    return response  # Status code success


# Route for submitting forms:
@forms.route('/listing-submit', methods=['POST'])
def listing_submit():
    """Listing submission route.
    This function handles the listing submissions.

    NOTE: The client-side should ensure that each field
    contains information.  The additional_info my be blank.

    Returns ListingsModel as JSON.
    """
    data = request.json

    # Client information:
    client_name = data['client_name']
    client_address = data['client_address']
    client_city = data['client_city']
    client_state = data['client_state']
    client_zip = data['client_zip']

    # Listing information:
    position_title = data['position_title']
    pos_responsibility = data['pos_responsibility']
    min_qualifications = data['min_qualifications']
    pref_qualifications = data['pref_qualifications']
    additional_info = data['additional_info']
    duration = data['duration']
    app_open = data['app_open']
    app_close = data['app_close']

    # Add client to database:
    client_full_address = f'{client_address}, {client_city}, {client_state},\
                            {client_zip}'
    client = ClientsModel(client_name, client_full_address)
    db.session.add(client)
    db.session.commit()

    # Add listing to database:
    tmp = ClientsModel.query.filter_by(client_name=client_name).first()
    listing_client_id = tmp.id
    listing = ListingsModel(listing_client_id, position_title,
                            pos_responsibility, min_qualifications,
                            pref_qualifications, additional_info,
                            status='pending', duration=duration,
                            app_open=app_open, app_close=app_close)
    db.session.add(listing)
    db.session.commit()

    response = {'status': 200}
    return response


# Route for submitting password reset:
@forms.route('/reset-password-submit', methods=['PUT'])
def reset_pass_submit():
    """Reset password submission route.
    This function handles the submission of a password reset.
    """
    data = request.json
    response = dict()
    user = UsersModel.query.filter_by(username=data['username']).first()
    if(user):
        if(data['password'] == data['passwordReEntered']):
            pass_hash = hashlib.sha256(data['password'].encode()).hexdigest()
            user.password = pass_hash
            db.session.commit()
            response['redirect'] = 'login.html'
            code = 200
        else:
            response['err_msg'] = 'Passwords do not match'
            code = 401
    else:
        response['err_msg'] = 'User not found in database'
        code = 403

    return response, code
