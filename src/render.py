import yaml
from jinja2 import Environment, FileSystemLoader

# SALMOS
with open("../data/salmos.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

salmos = {}
for salmo in data:
    salmos[salmo] = []
    for grupo in data[salmo]:
        salmos[salmo].append([p.strip() for p in grupo.split(",")])


# PALABRAS
with open("../data/palabras.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

palabras = {}
for palabra in data:
    palabras[palabra] = data[palabra]

# EUCARISTÍAS
with open("../data/eucaristía.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

eucaristias = []
for eucaristia in data:
    eucaristias.append(data[eucaristia])


env = Environment(loader=FileSystemLoader("../templates"))
template = env.get_template("index.html")
output = template.render(salmos=salmos, palabras=palabras, eucaristias=eucaristias)
with open("../index.html", "w", encoding='utf-8') as f:
    f.write(output)


