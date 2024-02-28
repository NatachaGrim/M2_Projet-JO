from ..app import app, db

class Formulaire(db.Model):
    __tablename__ = "formulaire"

    id_team = db.Column(db.String(45), primary_key=True, nullable = False, unique=True)
    noc = db.Column(db.String(3), db.ForeignKey('pays.noc'), nullable=False)
    year = db.Column(db.Integer)

    donnees = db.relationship('Donnees', backref='formulaire', lazy=True)
    medailles = db.relationship('Medailles', backref='donnees', lazy=True)
    
    def __repr__(self):
        return '<Formulaire %r>' % (self.id_team) 

class Pays(db.Model):
    __tablename__ = "pays"

    noc = db.Column(db.String(3), primary_key=True, nullable = False, unique=True)
    nom = db.Column(db.String(100))
    lattitude = db.Column(db.Float)
    longitude =db.Column(db.Float)

    formulaires = db.relationship('Formulaire', backref='pays', lazy=True)

    def __repr__(self):
        return '<Pays %r>' % (self.nom)
    
class Donnees(db.Model):
    __tablename__ = "donnees"

    id_team = db.Column(db.String(45), db.ForeignKey('formulaire.id_team'), nullable=False)
    population = db.Column(db.Integer)
    richesse = db.Column(db.Float)
    investissement = db.Column(db.Float)

    def __repr__(self):
        return 'Donnees %r>' % (self.id_team) 

class Medailles(db.Model):
    __tablename__ = "medailles"

    id_team = db.Column(db.String(45), db.ForeignKey('formulaire.id_team'), nullable=False)
    gold = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    bronze= db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __repr__(self):
        return '<Medailles %r>' % (self.id_team) 



