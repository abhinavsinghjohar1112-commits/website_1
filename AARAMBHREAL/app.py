# -------------------- IMPORTS --------------------
from flask import Flask, render_template, redirect, url_for
from models import db, Property, Lead
from forms import RegisterForm, ContactForm
from datetime import datetime


from config import Config

app = Flask(__name__)
app.config.from_object(Config)

 

db.init_app(app)


# -------------------- CREATE DATABASE --------------------
with app.app_context():
    db.create_all()


# -------------------- HOME ROUTE --------------------
@app.route('/')
def home():
    properties = Property.query.limit(4).all()  # show only featured
    return render_template('home.html', properties=properties)


# -------------------- ABOUT PAGE --------------------
@app.route('/about')
def about():
    return render_template('about.html')


# -------------------- ALL PROPERTIES --------------------
@app.route('/properties')
def properties():
    all_properties = Property.query.all()
    return render_template('properties.html', properties=all_properties)


# -------------------- PROPERTY DETAIL --------------------
@app.route('/property/<int:id>')
def property_detail(id):
    property = Property.query.get_or_404(id)
    return render_template('property_detail.html', property=property)


# -------------------- SEARCH --------------------
@app.route('/search')
def search():
    from flask import request   # imported here to keep top clean

    location = request.args.get('location', '')

    results = Property.query.filter(
        Property.location.ilike(f"%{location}%")
    ).all()

    return render_template('properties.html', properties=results)


# -------------------- REGISTER (LEAD FORM) --------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_lead = Lead(
            name=form.name.data,
            phone=form.phone.data,
            property=form.property.data,
            time=datetime.now()
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect(url_for('thank_you'))

    return render_template('register.html', form=form)


# -------------------- CONTACT --------------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # you can later store this in DB also
        print("Message:", form.message.data)

        return redirect(url_for('thank_you'))

    return render_template('contact.html', form=form)


# -------------------- THANK YOU PAGE --------------------
@app.route('/thankyou')
def thank_you():
    return render_template('result.html')


# -------------------- RUN APP --------------------
if __name__ == '__main__':
    app.run(debug=True)

 
