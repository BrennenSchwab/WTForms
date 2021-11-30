from flask import Flask, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from model import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY']= 'passwordnot'

toolbar = DebugToolbarExtension(app)

connect_db(app)

db.drop_all()
db.create_all()


@app.route('/')
def pet_list():
    """Show home page"""

    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """add a pet for adoption"""

    form = AddPetForm()
    
    if form.validate_on_submit():
        
        data = {d: c for d, c in form.data.items() if d != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} was added.")
        return redirect('/')
    
    else:
        return render_template("add_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} has been updated.")
        return redirect('/')

    else:
        
        return render_template("edit_form.html", form=form, pet=pet)
