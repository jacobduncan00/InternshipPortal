# Internship Portal Web App
# views.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan
"""


# Flask Imports:
from flask import render_template, Blueprint, request, redirect, url_for
from api import session

# Create views blueprint:
views = Blueprint('views', __name__)

# ------------------------------------------------------------------------
#                                 ROUTES
# ------------------------------------------------------------------------

# Root page route:


@views.route('/')
def root():
    """Root page view route.
    This function runs whenever the root page (url below) is requested.
        ex) -> localhost:5000/
    Returns the root page: which renders index.html (landing page)
    """
    return render_template('index.html', page_title='Internship Web Portal Homepage')


# Admin view route:
@views.route('/admin')
def admin():
    """Admin page view route.
    This function runs whenver the admin page ('/admin') is requested.
        ex) -> localhost:5000/admin
    Returns the admin page: which renders admin.html (admin dashboard)
    """
    if 'username' in session:
        return render_template('admin/admin.html', page_title='Admin Dashboard')
    else:
        return root()


# Admin Listings view route:
@views.route('/admin/listings')
def admin_listings():
    """Admin Listings page view route.
    This function runs whenver the admin page ('/admin/listings') is requested.
        ex) -> localhost:5000/admin/listings
    """
    if 'username' in session:
        return render_template('admin/admin_listings.html', page_title='Admin Dashboard | Listings')
    else:
        return root()


@views.route('/admin/edit/listing')
def admin_edit_listing():
    """Admin Edit Listing page view route.
    This function runs whenver the admin page ('/admin/edit/listing') is requested.
        ex) -> localhost:5000/admin/edit/listing
    """
    if 'username' in session:
        return render_template('admin/edit_listing.html', page_title='Admin Dashboard | Edit Listing')
    else:
        return root()


# Renders login page for admin:
@views.route('/login', methods=['GET'])
def login():
    """Login page for admin.
    This function runs whenver the login page ('/login') is requested.
        ex) -> localhost:5000/admin
    Returns the login page: which renders login.html (login form)
    """
    return render_template('login.html', page_title='Admin Login')


# Renders contact page:
@views.route('/contact', methods=['GET'])
def contact():
    """Contact page for users.
    This function runs whenver the contact page ('/contact') is requested.
        ex) -> localhost:5000/contact
    Returns the login page: which renders contact.html (contact page)
    """
    return render_template('contact.html', page_title='Contact Us')


# Renders insert internship page:
@views.route('/insert-listing', methods=['GET'])
def insert_internship():
    """Insert internship page for users.
    This function runs whenver the insert-listing page ('/insert-listing') is requested.
        ex) -> localhost:5000/insert-listing
    Returns the login page: which renders insert_listing.html (insert listing page)
    """
    return render_template('insert_listing.html', page_title='Request Internship Listing')
