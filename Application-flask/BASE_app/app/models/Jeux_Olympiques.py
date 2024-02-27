from ..app import app, db


#Reste à définir les clés étrangères et à documenter les classes 

class Donnees(db.Model):
    __tablename__ = "donnees"

    id = db.Column(db.String(45), primary_key=True, nullable = False, unique=True)
    population = db.Column(db.Integer)
    richesse = db.Column(db.Float)
    investissement = db.Column(db.Float)

    # propriétés de relation (à ajouter)
    areas = db.relationship('Area',  backref='areas',  lazy=True)
    

    def __repr__(self):
        return '<Donnees %r>' % (self.id) 

class Formulaire(db.Model):
    __tablename__ = "Formulaire"

    id = db.Column(db.String(45))
    noc = db.Column(db.String(3))
    year = db.Column(db.DateTime)
    
    # propriétés de relation (à ajouter)

    def __repr__(self):
        return '<Formulaire %r>' % (self.noc) 

class Medailles(db.Model):
    __tablename__ = "medailles"

    id = db.Column(db.String(45)) 
    gold = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    bronze= db.Column(db.Integer)
    total = db.Column(db.Integer)

    # propriétés de relation (à ajouter)

    def __repr__(self):
        return '<Boundaries %r>' % (self.total) 

class Pays(db.Model):
    __tablename__ = "pays"

    noc = db.Column(db.String(3))
    nom = db.Column(db.String(100))
    lattitude = db.Column(db.Float)
    longitude =db.Column(db.Float)

    # propriétés de relation (à ajouter)


   
    def __repr__(self):
        return '<Pays %r>' % (self.nom)
