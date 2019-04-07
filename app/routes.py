from flask import jsonify
from app import db
from app import app
from .models import ForeignPhrase
from .translate_api_helper import translate, language_code_from_phrase, language_name_from_code


@app.route('/translate/<phrase>')
def submit_phrase(phrase):
    language_code = language_code_from_phrase(phrase)
    language_name = language_name_from_code(language_code)
    translated_phrase = translate(
        phrase=phrase,
        from_language=language_code)
    foreign_phrase_record = ForeignPhrase(
        original_message=phrase,
        original_language=language_name,
        english_translation=translated_phrase)
    db.session.add(foreign_phrase_record)
    db.session.commit()
    return jsonify(dict(data=translated_phrase))

@app.route('/translations', defaults={'page': 1, 'num_items': 20})
@app.route('/translations/<int:page>/<int:num_items>')
def translations(page, num_items):
    if num_items > 50:
        return jsonify(dict(data='Too many items')), 401
    translations = ForeignPhrase.paginate_translations(page, num_items)
    return jsonify(dict(data=translations))
