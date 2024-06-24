# 1 вариант
from jinja2 import Environment, FileSystemLoader

htmls = [
    {"type": "text", "name": "firstname", "placeholder": "Имя"},
    {"type": "text", "name": "lastname", "placeholder": "Фамилия"},
    {"type": "text", "name": "address", "placeholder": "Адрес"},
    {"type": "tel", "name": "phone", "placeholder": "Телефон"},
    {"type": "email", "name": "email", "placeholder": "Почта"}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(htmls=htmls)

print(msg)


#  2 вариант
# from jinja2 import Template
#
# htmls = [
#     {"type": "text", "name": "firstname", "placeholder": "Имя"},
#     {"type": "text", "name": "lastname", "placeholder": "Фамилия"},
#     {"type": "text", "name": "address", "placeholder": "Адрес"},
#     {"type": "tel", "name": "phone", "placeholder": "Телефон"},
#     {"type": "email", "name": "email", "placeholder": "Почта"}
# ]
#
# html = """
# {% macro dialog(type, name, placeholder) -%}
#     <p><input type="{{ type }}" name="{{ name }}" placeholder="{{ placeholder }}"></p>
# {% endmacro -%}
# {% for h in htmls -%}
#     {{ dialog(h.type, h.name, h.placeholder) }}
# {% endfor -%}
# """
#
# tm = Template(html)
# msg = tm.render(htmls=htmls)
#
# print(msg)