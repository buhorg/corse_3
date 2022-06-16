import json
import exeptions


class CommentsDAO:
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

    def get_all(self):
        return self.load_data()

    def get_comments_by_post_id(self, post_id):
        comments = self.load_data()
        comments_by_post_id = []
        for comment in comments:
            if comment['post_id'] == post_id:
                comments_by_post_id.append(comment)
        return comments_by_post_id
