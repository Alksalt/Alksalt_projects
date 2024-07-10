import re
import codecs
def delete_html_tags(html_file, result_file):
    with codecs.open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    new_file = re.sub(r'<[^<]+?>', ' ',html)
    new_file = re.sub(r'\s+', ' ', new_file)
    new_file = new_file.strip()

    with codecs.open(result_file, 'w', encoding='utf-8') as file:
        file.write(new_file)

html_file = "draft.html"
result_file = "result.txt"
delete_html_tags(html_file, result_file)

