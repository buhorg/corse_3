from flask import render_template, Blueprint, current_app, request

from app.bookmarks.dao.bookmarks_DAO import BookmarksDAO
from app.index.dao.post_dao import PostDAO
from app.index.utils import create_field_is_bookmark

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search/')
def search_1_page():
    data = PostDAO(current_app.config.get('PATH_TO_DATA'))
    text = request.args.get('s')
    if text:
        posts = data.get_post_by_text(text)
        bookmarks = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS')).get_all()
        posts = create_field_is_bookmark(posts, bookmarks)
        return render_template("search.html", text=text, posts=posts, count_posts=len(posts))
    else:
        return render_template("search.html", count_posts=0, text="Ищем строку")

