from collections import Counter
from functools import reduce


def format_news_data(news_list: list[dict]) -> list[dict]:
    formatted_news = []
    for news_item in news_list:
        if news_item["start_date"][-1] in '02468':
            news = {
                "name_ru": news_item["name_ru"],
                "html_ru": news_item["html_ru"],
                "start_date": news_item["start_date"]}
            formatted_news.append(news)
    return formatted_news


def get_largest_text(news_list: list[dict]) -> str:
    return max(news_list, key=lambda news_item: len(news_item["html_ru"]))["html_ru"]


def get_largest_title(news_list: list[dict]) -> str:
    return max(news_list, key=lambda news_item: len(news_item["name_ru"].split()))["name_ru"]


def get_most_common_letter(news_list: list[dict]) -> str:
    all_titles = reduce(lambda x,y: x + y, [news_item['name_ru'].lower() for news_item in news_list])
    most_common = Counter(all_titles.replace(' ', '')).most_common(1)
    return most_common
