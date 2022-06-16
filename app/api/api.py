import logging

from flask import current_app, jsonify, Blueprint

import exeptions
from app.api import loggers
from app.index.dao.post_dao import PostDAO

api_blueprint = Blueprint('api_blueprint', __name__)
logger = loggers.create_logger()


@api_blueprint.route('/api/post/<int:post_id>')
def api_post_page(post_id):
    logger = logging.getLogger('basic')
    logger.info(f"Запрос данных  из json файла на сервере")
    posts = PostDAO(current_app.config.get('PATH_TO_DATA'))
    logger.info(f"Данные имеющихся постов получены. Выполняется получение поста с id = {post_id}")
    post = posts.get_posts_by_id(post_id)
    return jsonify(post)


@api_blueprint.route('/api/posts/')
def api_posts_page():
    logger = logging.getLogger('basic')
    logger.info(f"Выполняется получение постов  из json файла на сервере")
    posts = PostDAO(current_app.config.get('PATH_TO_DATA')).get_all()
    return jsonify(posts)


@api_blueprint.errorhandler(exeptions.DataSourceBroken)
def data_source_broken(e):
    logger = logging.getLogger('basic')
    logger.error(f"Ошибка загрузки json-файла")
    return "Ошибка загрузки файла. Файл не найден или не в формате json"


