# Реализуйте абстракцию для работы с URL. Она должна извлекать и менять
# части адреса.
# Интерфейс:
# make(url) - Конструктор. Создает URL.
# get_scheme(data) - Селектор (геттер). Извлекает схему.
# set_scheme(data, scheme) - Сеттер. Меняет схему.
# get_host(data) - Геттер. Извлекает host.
# set_host(data, host) - Сеттер. Меняет host.
# get_path(data) - Геттер. Извлекает путь.
# set_path(data, path) - Сеттер. Меняет путь.
# get_query_param(data, param_name, default=None) - Геттер. Извлекает значение
# для параметра запроса. Третьим параметром функция принимает значение по
# умолчанию, которое возвращается тогда, когда в запросе не было такого
# параметра
# set_query_param(data, key, value) - Сеттер. Устанавливает значение для
# параметра запроса. Если передано значение None, то параметр отбрасывается.
# to_string(data) - Геттер. Преобразует URL в строковой вид.
# Все сеттеры должны возвращать новый изменённый URL, а старый оставлять
# неизменным.

from urllib.parse import urlparse, parse_qs, urlencode


def to_string(url_parsed):
    return url_parsed.geturl()


def make(url_string):
    return urlparse(url_string)


def get_scheme(url_parsed):
    return url_parsed.scheme


def set_scheme(url_parsed, scheme):
    return url_parsed._replace(scheme=scheme)


def get_host(url_parsed):
    return url_parsed.hostname


def set_host(url_parsed, host):
    return url_parsed._replace(netloc=host)


def get_path(url_parsed):
    return url_parsed.path


def set_path(url_parsed, path):
    return url_parsed._replace(path=path)


def get_query_param(url_parsed, query, default=None):
    try:
        return ''.join(parse_qs(url_parsed.query)[query])
    except KeyError:
        return default


def set_query_param(url_parsed, query_param, new_query):
    query = parse_qs(url_parsed.query)
    query[query_param] = new_query
    if new_query is None:
        query.pop(query_param)
    return url_parsed._replace(query=urlencode(query=query, doseq=True))
