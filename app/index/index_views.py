from flask import render_template, Blueprint, current_app
from .dao.post_dao import PostDAO
from app.post.dao.comments_dao import CommentsDAO
from app.bookmarks.dao.bookmarks_DAO import BookmarksDAO
from .utils import create_field_is_bookmark

index_blueprint = Blueprint('index_blueprint', __name__, template_folder='templates')


@index_blueprint.route('/')
def index_page():
    posts = PostDAO(current_app.config.get('PATH_TO_DATA'))
    data = CommentsDAO(current_app.config.get('PATH_TO_COMMENTS'))
    bookmarks = BookmarksDAO(current_app.config.get('PATH_TO_BOOKMARKS')).get_all()
    comments = data.get_all()
    # получаем короткий текст и кол-во комментариев. все #-слова из текста вынесены вперед
    all_posts = posts.get_short_content_and_comments_count(comments)
    # создаем ключ есть ли закладка, в зависимости от этого при нажатии на иконку будет либо добавляться,
    # либо удалятся закладка
    all_posts = create_field_is_bookmark(all_posts, bookmarks)
    return render_template("index.html", all_posts=all_posts, book_len=len(bookmarks))
