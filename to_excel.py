import pandas as pd


def data_to_excel(largest_text, largest_title, most_common_letter):
    df = pd.DataFrame(
        {'Largest Text': largest_text,
         'Largest Title': largest_title,
         'Most common letter': most_common_letter})
    df.to_excel('./data.xlsx')
