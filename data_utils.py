import formatter

import json
def get_title_text():
    titles = []
    json_file = "cnn.json"
    for titles_info in json.load(open(json_file)):
        titles.append(formatter.format_headline(titles_info['headline']))

    return " ".join(titles)
