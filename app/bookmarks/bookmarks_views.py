from flask import render_template, Blueprint, jsonify, current_app, request
from werkzeug.utils import redirect

from .dao.bookmarks_DAO import BookmarksDAO
from app.index.dao.post_dao import PostDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route('/bookmarks/')
def bookmarks_page():
    data = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS'))
    bookmarks = data.get_short_content()
    return render_template('bookmarks.html', bookmarks=bookmarks)


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>')
def create_bookmark(post_id):
    posts = PostDAO(current_app.config.get('PATH_TO_DATA'))
    post = posts.get_posts_by_id(post_id)
    data_bookmarks = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS'))
    data_bookmarks.add_or_remove_bookmark(post)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>')
def delete_book(post_id):
    data = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS'))
    data.del_bookmark(post_id)
    return redirect("/bookmarks/", code=302)

