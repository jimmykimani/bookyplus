from flask import Blueprint

bookmark = Blueprint('bookmark', __name__)

from . import views
from ..models import Tag

@bookmark.app_context_processor
def inject_tags():
    return dict(all_tags=Tag.all)