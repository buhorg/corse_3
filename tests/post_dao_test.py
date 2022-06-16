from app.index.dao.post_dao import PostDAO
import pytest


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostDAO('./data/data.json')
    return posts_dao_instance


keys_should_be = {"pk", "poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count"}


class TestPostDao:

    def test_get_all(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert keys_should_be <= set(posts[0].keys()), "неверный список ключей"

    def test_get_by_id(self, posts_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        post = posts_dao.get_posts_by_id(1)
        assert type(post) == dict, "возвращается не словарь"
        assert (post["pk"] == 1), "возвращается неправильный пост"
        assert keys_should_be <= set(post.keys()), "неверный список ключей"
