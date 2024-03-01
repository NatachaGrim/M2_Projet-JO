from ..app import app, db

class Formulaire(db.Model):
    """
    Classe centrale, représentant tous les pays des jeux olympiques, identifiés par l'assemblage de leur NOC et l'année de leur participation.

    Attributes
    ----------
    id_team : db.Column
        Identifiant unique de l'équipe, clé primaire.
    noc : db.Column
        Code du Comité National Olympique, clé étrangère reliant à la table 'pays'.
    year : db.Column
        Année de participation de l'équipe.
    donnees : db.relationship
        Relation avec la classe 'Donnees', représentant les données de l'équipe.
    medailles : db.relationship
        Relation avec la classe 'Medailles', représentant les médailles gagnées par l'équipe.

    Methods
    -------
    __repr__(self)
        Représente l'instance de Formulaire par son identifiant d'équipe.
    """

    __tablename__ = "formulaire"

    id_team = db.Column(db.String(45), primary_key=True, nullable=False, unique=True)
    noc = db.Column(db.String(3), db.ForeignKey('pays.noc'), nullable=False)
    year = db.Column(db.Integer)

    donnees = db.relationship('Donnees', backref='formulaire', lazy=True)
    medailles = db.relationship('Medailles', backref='donnees', lazy=True)
    
    def __repr__(self):
        return '<Formulaire %r>' % (self.id_team) 

class Pays(db.Model):
    """
    Une classe représentant un pays participant aux jeux olympiques.

    Attributes
    ----------
    noc : db.Column
        Code du Comité National Olympique, clé primaire et unique.
    nom : db.Column
        Nom du pays.
    lattitude : db.Column
        Latitude géographique du pays.
    longitude : db.Column
        Longitude géographique du pays.
    formulaires : db.relationship
        Relation avec la classe 'Formulaire', représentant les formulaires liés au pays.

    Methods
    -------
    __repr__(self)
        Représente l'instance de Pays par son nom.
    """

    __tablename__ = "pays"

    noc = db.Column(db.String(3), primary_key=True, nullable=False, unique=True)
    nom = db.Column(db.String(100))
    lattitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    formulaires = db.relationship('Formulaire', backref='pays', lazy=True)

    def __repr__(self):
        return '<Pays %r>' % (self.nom)
    
class Donnees(db.Model):
    """
    Une classe représentant les données d'une équipe participant aux jeux olympiques.

    Attributes
    ----------
    id_team : db.Column
        Identifiant unique de l'équipe, clé étrangère reliant à la table 'formulaire'.
    population : db.Column
        Population du pays de l'équipe.
    richesse : db.Column
        Richesse du pays de l'équipe.
    investissement : db.Column
        Investissement dans l'équipe.

    Methods
    -------
    __repr__(self)
        Représente l'instance de Donnees par son identifiant d'équipe.
    """

    __tablename__ = "donnees"

    id_team = db.Column(db.String(45), db.ForeignKey('formulaire.id_team'), nullable=False)
    population = db.Column(db.Integer, primary_key=True)
    richesse = db.Column(db.Float)
    investissement = db.Column(db.Float)

    def __repr__(self):
        return 'Donnees %r>' % (self.id_team) 

class Medailles(db.Model):
    """
    Une classe représentant les médailles gagnées par une équipe aux jeux olympiques.

    Attributes
    ----------
    id_team : db.Column
        Identifiant unique de l'équipe, clé étrangère reliant à la table 'formulaire'.
    gold : db.Column
        Nombre de médailles d'or gagnées.
    silver : db.Column
        Nombre de médailles d'argent gagnées.
    bronze : db.Column
        Nombre de médailles de bronze gagnées.
    total : db.Column
        Nombre total de médailles gagnées.

    Methods
    -------
    __repr__(self)
        Représente l'instance de Medailles par son identifiant d'équipe.
    """

    __tablename__ = "medailles"

    id_team = db.Column(db.String(45), db.ForeignKey('formulaire.id_team'), nullable=False)
    gold = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    bronze = db.Column(db.Integer)
    total = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Medailles %r>' % (self.id_team)
