from flask import render_template, Blueprint, current_app
from app.index.dao.post_dao import PostDAO
from .dao.comments_dao import CommentsDAO
from ..bookmarks.dao.bookmarks_DAO import BookmarksDAO
from ..index.utils import create_field_is_bookmark

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/post/<int:post_id>')
def post_page(post_id):
    posts = PostDAO(current_app.config.get('PATH_TO_DATA'))
    comments = CommentsDAO(current_app.config.get('PATH_TO_COMMENTS'))
    post = posts.get_posts_by_id(post_id)
    comments_by_post_id = comments.get_comments_by_post_id(post_id)
    bookmarks = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS')).get_all()
    post = create_field_is_bookmark([post], bookmarks)[0]
    return render_template("post.html", post=post, comments_by_post_id=comments_by_post_id,
                           comment_count=len(comments_by_post_id))

