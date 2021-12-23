# Justin Ventura

"""
This module contains routes specifically for the admin.  This
means that the admin must be logged in (session is active) in
order to access these routes.  The requester must of course be
that logged in admin.
"""

# Flask imports:
from flask import Blueprint, request

from .models import db, ListingsModel, ContactFormMessage
from .constants import LISTING_STATUSES
from .helpers import admin_session


admin = Blueprint('admin', __name__, url_prefix='/admin')


# ------------------------------------------------------------------------
#          ADMIN ROUTES: these routes are all for the admin
# ------------------------------------------------------------------------

# Ensure that client is in admin session:
@admin.before_request
def _admin_session():
    """Runs before all admin routes to check session."""
    if admin_session() is False:
        return {'err_msg': 'ACCESS DENIED.'}, 403


# Route for changing a listings status.
@admin.route('/set-status/<id>/<status>', methods=['PUT'])
def action_on_listing(id: int, status: str):
    """Route accepts a listing:

    NOTE: must be in admin session.
    """
    response = dict()

    # Valid status:
    if status in LISTING_STATUSES:
        listing = ListingsModel.query.get(id)
        listing.status = status
        db.session.commit()

        response['listing'] = listing.to_dict()
        code = 200

    # Invalid status:
    else:
        response['err_msg'] = 'Invalid status'
        code = 400

    return response, code


# Route for (un)starring listings.
@admin.route('star-listing/<listing_id>', methods=['PUT'])
def star_listing(listing_id: int):
    """Star a listing

    If a listing is unstarred, star it.
    If a listing is starred, unstar it.
    """
    response = dict()

    # Check if listing is in database, then update and return to Jake:
    if listing := ListingsModel.query.filter_by(id=listing_id).first():
        listing.starred = True if listing.starred is False else False
        db.session.commit()
        response['listing'] = listing.to_dict()
        code = 200

    # Otherwise, return an error message:
    else:
        response['err_msg'] = f'Listing with id {listing_id}\
                                not found in database'
        code = 400

    return response, code


# Route for editing listings.
@admin.route('edit-listing/<id>', methods=['PUT'])
def edit_listing(id: int) -> None:
    """Edit a listing.

    Replace the existing listing data with the data
    passed in with the request."""
    response = dict()
    data = request.json

    assert data is not None, 'No listing information in PUT request.'

    # If the listing is already in the database:
    if listing := ListingsModel.query.filter_by(id=id).first():

        # Listing information:
        listing.position = data['position_title']
        listing.pos_responsibility = data['pos_responsibility']
        listing.min_qualifications = data['min_qualifications']
        listing.pref_qualifications = data['pref_qualifications']
        listing.additional_info = data['additional_info']
        listing.duration = data['duration']
        listing.app_open = data['app_open']
        listing.app_close = data['app_close']

        # Update the database.
        db.session.commit()
        response['listing'] = listing.to_dict()
        code = 200

    # Invalid listing id:
    else:
        response['err_msg'] = f'Listing with id {id}\
                                not found in database'
        code = 400

    return response, code


@admin.route('get-messages/<message_filter>', methods=['GET'])
def get_messages(message_filter: str = 'all'):
    """
    Admin route for receiving messages

    TODO: Test this route and ensure that it works with front end.
    """
    response = dict()
    messages = list()

    # For querying all messages:
    if message_filter == 'all':
        messages = ContactFormMessage.query.all()

    # For querying just messages labelled as unseen.
    elif message_filter == 'unseen':
        messages = ContactFormMessage.query.filter(was_seen=False)
        # TODO: label as seen?

    # Catch incorrect requests.
    else:
        response['err_msg'] = 'Invalid contact form message request'
        return response, 400

    # Return messages, if there are any.
    if messages is not None:
        code = 200

        for i, message in enumerate(messages):

            response[i] = message.to_dict()

    else:
        response['err_msg'] = 'No messages found.'
        code = 200

    return response, code
