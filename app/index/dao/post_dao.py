import json
import exeptions
from app.index.utils import ending_for_word_comment, rewrite_text_without_tag_words, rewrite_tag_word_to_link
from app.index.utils import find_hash_tag_word


class PostDAO:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"Работа с файлом {self.path}"

    def load_data(self):
        try:
            with open(self.path, encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise exeptions.DataSourceBroken("Ошибка загрузки файла. Файл не найден или не в формате json")
        else:
            return data

    def get_all(self):
        return self.load_data()

    def get_short_content(self):
        """
        Получаем короткий текст, все #-слова вынесены вперед. Если #-слов много, то выводим столько,
        чтобы слова оказались цельными и не превысила общая длина 50
        """
        posts = self.load_data()
        for post in posts:
            hash_tag_words = find_hash_tag_word(post['content'])
            tag_words = " ".join(hash_tag_words)
            print(tag_words)
            if len(tag_words) > 50:
                len_tag_words = 0
                post['short_content'] = ''
                for word in hash_tag_words:
                    len_tag_words += len(word)
                    if len_tag_words < 50:
                        post['short_content'] = word + ' ' + post['short_content']
                    else:
                        break
                post['short_content'] = rewrite_tag_word_to_link(post['short_content'])
            else:
                post['short_content'] = post['content']
                post['short_content'] = rewrite_text_without_tag_words(post['short_content'], hash_tag_words)
                post['short_content'] = tag_words + ' ' + post['short_content']
                if len(post['short_content']) > 50:
                    post['short_content'] = post['short_content'][0:50]
                post['short_content'] = rewrite_tag_word_to_link(post['short_content'])
        return posts

    def get_short_content_and_comments_count(self, comments):
        posts = self.get_short_content()
        for post in posts:
            count = 0
            for comment in comments:
                if post['pk'] == comment['post_id']:
                    count += 1
            post['comments_count'] = ending_for_word_comment(count)
        return posts

    def get_posts_by_user(self, user_name):
        posts = self.get_short_content()
        user_posts = []
        for post in posts:
            if post['poster_name'].lower() == user_name.lower():
                user_posts.append(post)
        return user_posts

    def get_posts_by_id(self, pk):
        posts = self.load_data()
        for post in posts:
            if post['pk'] == pk:
                post['content_link'] = rewrite_tag_word_to_link(post['content'])
                return post

    def get_post_by_text(self, text):
        data = self.get_short_content()
        posts = []
        for post in data:
            if post['content'].lower().count(text.lower()):
                posts.append(post)
                if len(posts) == 10:
                    return posts
        return posts

    def get_posts_by_tag(self, uid):
        data = self.get_short_content()
        posts = []
        for post in data:
            hash_tag_words = find_hash_tag_word(post['content'])
            if len(hash_tag_words) > 0:
                if ('#' + uid) in hash_tag_words:
                    posts.append(post)
        return posts
