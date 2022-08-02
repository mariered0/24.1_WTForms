from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pets_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def homepage():
    """Show homepage with a list of pets."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Show a form to add pets."""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data

        photo_url = form.photo_url.data
        notes = form.notes.data
        
        pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes)
        db.session.add(pet)
        db.session.commit()
        
        flash(f"Created a new pet: A {species} named {name}")
        
        return redirect('/')

    else:
        return render_template(
            "add_pet_form.html", form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet_details(id):
    """Show a page with the details of the pet."""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        
        flash(f"{pet.name} updated.")
        
        return redirect('/')
    
    else:
        return render_template('pet_details.html', pet=pet, form=form)


