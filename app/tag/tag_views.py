from flask import render_template, Blueprint, current_app

from app.bookmarks.dao.bookmarks_DAO import BookmarksDAO
from app.index.dao.post_dao import PostDAO
from app.index.utils import create_field_is_bookmark

tag_blueprint = Blueprint('tag_blueprint', __name__, template_folder='templates')


@tag_blueprint.route('/tag/<uid>')
def tag_page(uid):
    data = PostDAO(current_app.config.get('PATH_TO_DATA'))
    posts = data.get_posts_by_tag(uid)
    bookmarks = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS')).get_all()
    posts = create_field_is_bookmark(posts, bookmarks)
    return render_template('tag.html', posts=posts, tag=uid)
