from datetime import datetime
from app import db


class ForeignPhrase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_message = db.Column(db.String(2000))
    original_language = db.Column(db.String(30))
    english_translation = db.Column(db.String(3000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @classmethod
    def paginate_translations(cls, page=1, num_items=20):
        phrase_translations = db.session.query(cls).\
            order_by(cls.timestamp.desc()).\
            paginate(page, num_items, False).items
        phrase_translations_dict = [{
            "original_message": pt.original_message,
            "original_language": pt.original_language,
            "english_translation": pt.english_translation}
            for pt in phrase_translations]
        return phrase_translations_dict

    def __repr__(self):
        return f'<{self.original_message}({self.original_language})-->{self.english_translation}(English)>'
