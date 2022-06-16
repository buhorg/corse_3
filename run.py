import dotenv
import os
from flask import Flask

from app.api.api import api_blueprint
from app.index.index_views import index_blueprint
from app.post.post_views import post_blueprint
from app.user_feed.user_feed_views import user_feed_blueprint
from app.tag.tag_views import tag_blueprint
from app.search.search_views import search_blueprint
from app.bookmarks.bookmarks_views import bookmarks_blueprint

app = Flask(__name__)
dotenv.load_dotenv(override=True)
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')

app.register_blueprint(index_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(tag_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def http_404_handler(e):
    return "<p>HTTP 404 Error Encountered</p>", 404


@app.errorhandler(500)
def http_500_handler(e):
    return "<p>HTTP 500 Error Encountered</p>", 500


if __name__ == '__main__':
    app.run()
