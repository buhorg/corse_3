def ending_for_word_comment(num):
    """
    Правильные окончания в слове комментарий в зависимости от числительного
    """
    if num == 0:
        return 'Нет комментариев'
    elif ((num >= 5) and (num <= 20)) or ((num > 100) and ((num % 100 >= 11) and (num % 100 <= 14))):
        return f'{num} комментариев'
    elif ((num >= 2) and (num <= 4)) or ((num % 10 >= 2) and (num % 10 <= 4)):
        return f'{num} комментария'
    elif (num == 1) or (num % 10 == 1):
        return f'{num} комментарий'
    else:
        return f'{num} комментариев'


def find_hash_tag_word(text):
    """
    Поиск и составление списка из #-слов
    """
    words = text.split(' ')
    hash_tag_words = []
    for word in words:
        if (word != '') and (word[0] == '#'):
            hash_tag_words.append(word)
    return hash_tag_words


def change_hash_tag_word_to_link(words):
    """
    меняем #-слова на ссылки служебная для следующей функции
    """
    link_words = []
    for word in words:
        link = f"<a href='/tag/{word[1:len(word)]}' class= 'item__tag'>{word}</a>"
        link_words.append(link)
    return link_words


def rewrite_tag_word_to_link(text):
    """
    меняем  в тексте #-слова на ссылки
    """
    words = text.split(' ')
    new_words = []
    for word in words:
        if (word != '') and (word[0] == '#'):
            new_words.append(change_hash_tag_word_to_link([word])[0])
        else:
            new_words.append(word)
    new_text = ' '.join(new_words)
    return new_text


def rewrite_text_without_tag_words(text, tag_words):
    """
    Переписываем текст без #-слов.
    """
    words = text.split(' ')
    new_words = []
    for word in words:
        if not (word in tag_words):
            new_words.append(word)
    new_text = ' '.join(new_words)
    return new_text


def create_field_is_bookmark(posts, bookmarks):
    """
    Добавляем ключ is_bookmark (есть ли у поста закладка)
    """
    for post in posts:
        post['is_bookmark'] = 0
        for bookmark in bookmarks:
            if post['pk'] == bookmark['pk']:
                post['is_bookmark'] = 1
                break
    return posts
