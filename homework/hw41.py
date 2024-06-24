from jinja2 import Template

hrefs = [
    {'href': 'index', 'title': 'Главная'},
    {'href': 'news', 'title': 'Новости'},
    {'href': 'about', 'title': 'О компании'},
    {'href': 'shop', 'title': 'Магазин'},
    {'href': 'contacts', 'title': 'Контакты'}
]


link = """
<ul>
{% for h in hrefs -%}
{% if h.title == 'Главная' -%}
<li><a href="/{{ h['href'] }}" class="active">{{ h['title'] }}</a></li>
{% else -%}
<li><a href="/{{ h['href'] }}">{{ h['title'] }}</a></li>
{% endif -%}
{% endfor -%}
</ul>"""

tm = Template(link)
msg = tm.render(hrefs=hrefs)

print(msg)

