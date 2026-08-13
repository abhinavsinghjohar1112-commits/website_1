from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


# -------------------- REGISTER FORM --------------------
class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    
    property = StringField('Property Interested In', validators=[DataRequired(), Length(max=100)])
    
    submit = SubmitField('Submit')


# -------------------- CONTACT FORM --------------------
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=5, max=500)])
    
    submit = SubmitField('Send Message')