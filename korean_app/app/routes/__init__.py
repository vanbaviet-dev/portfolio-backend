from .word_route import word_bp


def register_routes(app):
    app.register_blueprint(word_bp)
