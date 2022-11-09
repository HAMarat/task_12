import json

POST_PATH = 'posts.json'


def load_json_posts() -> list[dict]:
    """
    Загружаем данные из json файла
    """
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def find_posts(text_search: str) -> list[dict]:
    """
    Ищем посты в которых содержится искомый ключ поиска
    """
    find_posts_dict = []
    for post in load_json_posts():
        if text_search in post["content"]:
            find_posts_dict.append(post)
    return find_posts_dict


def append_json_data(path: str, text: str) -> None:
    """
    Добавляем данные нового поста в json файл
    """
    json_data = load_json_posts()
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        post_dict = {'pic': path, 'content': text}
        json_data.append(post_dict)
        json.dump(json_data, file, ensure_ascii=False, indent=4)
        return

