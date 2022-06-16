class TestPosts:

    def test_all_posts_status(self, test_client):
        """ Проверяем, получается ли при запросе кандидатов нужный статус-код """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

    def test_single_post_status(self, test_client):
        """ Проверяем, получается ли при запросе одного поста нужный статус-код """
        response = test_client.get('/post/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса одного поста неверный"
