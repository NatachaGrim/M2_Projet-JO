from ..app import app, db
from flask import render_template

@app.errorhandler(404)
def not_found_error(error):
	""" Gestion des erreurs 404
	
	:param error: Objet d'erreur
	:type error: Exception
	:returns: Page HTML correspondant au type d'erreur 404
	"""
	return render_template('404.html'), 404

@app.errorhandler(500)
@app.errorhandler(503)
def internal_error(error):
	""" Gestion des erreurs de serveur type 500 incluant un rollback sur la base de données.
	
	:param error: Objet d'erreur
	:type error: Exception
	:returns: Page HTML correspondant au type d'erreur 500
	"""
	db.session.rollback()
	return render_template('500.html'), 500
