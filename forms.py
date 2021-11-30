from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddPetForm(FlaskForm):

    name = StringField("Name of Pet", validators=[InputRequired()], render_kw={"class":"form-control"})
    species = SelectField(
        "Pet type", 
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")], 
        render_kw={"class":"form-select"},
        )
    photo_url = StringField("Photo URL", validators=[Optional(), URL()], render_kw={"class":"form-control"})
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)], render_kw={"class":"form-control"})
    notes = TextAreaField("Notes", validators=[Optional()], render_kw={"class":"form-control"})

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()], render_kw={"class":"form-control"})

    notes = TextAreaField("Notes", validators=[Optional()], render_kw={"class":"form-control mb-2"})

    available = BooleanField(
        "Available?", 
        render_kw={"class":"form-check-input", "type": "checkbox"},
        )