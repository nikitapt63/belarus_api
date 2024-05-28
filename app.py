from core import get_api_news_data
from main import get_largest_text, get_largest_title, get_most_common_letter, format_news_data
from to_excel import data_to_excel


def run():
    data = get_api_news_data()
    format_data = format_news_data(data)
    text = get_largest_text(format_data)
    title = get_largest_title(format_data)
    letter = get_most_common_letter(format_data)
    data_to_excel(largest_text=text, largest_title=title, most_common_letter=letter)


run()
