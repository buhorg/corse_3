import json
import exeptions
from app.index.utils import find_hash_tag_word, rewrite_tag_word_to_link, rewrite_text_without_tag_words


class BookmarksDAO:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        try:
            with open(self.path, encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            raise exeptions.DataSourceBroken("Ошибка загрузки файла. Файл не найден или не в формате json")
        else:
            return data

    def write_data_json(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_all(self):
        return self.load_data()

    def get_bookmarks_by_post_id(self, post_id):
        data = self.load_data()
        bookmarks_by_post_id = []
        for bookmark in data:
            if bookmark['post_id'] == post_id:
                bookmarks_by_post_id.append(bookmark)
        return bookmarks_by_post_id

    def is_bookmark(self, post):
        data = self.load_data()
        for bookmark in data:
            if bookmark['pk'] == post['pk']:
                return True
        return False

    def add_or_remove_bookmark(self, post):
        if not self.is_bookmark(post):
            new_bookmark = {'pk': post['pk'], 'poster_name': post['poster_name'],
                            'poster_avatar': post['poster_avatar'],
                            'pic': post['pic'], 'content': post['content'], 'views_count': post['views_count']}
            data = self.load_data()
            data.append(new_bookmark)
            self.write_data_json(data)
            return data
        else:
            data = self.del_bookmark(post['pk'])
            return data

    def del_bookmark(self, post_id):
        data = self.get_all()
        enum_list = enumerate(data)
        for index, bookmark in enum_list:
            if bookmark['pk'] == post_id:
                data.pop(index)
        self.write_data_json(data)
        return data

    def get_short_content(self):
        posts = self.get_all()
        for post in posts:
            hash_tag_words = find_hash_tag_word(post['content'])
            tag_words = " ".join(hash_tag_words)
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
