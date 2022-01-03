# `'age_upon_outcome'` — возраст животного на момент прибытия в приют.
# `'animal_id'` — идентификатор животного.
# `'animal_type'` — тип животного.
# `'name'` — кличка.
# `'breed'` — порода.
# `'color1', 'color2'` — цвет или сочетание цветов.
# `'date_of_birth'` — дата рождения.
# `'outcome_subtype'` — программа, в которой участвует животное.
# `'outcome_type'` — что сейчас с животным.
# `'outcome_month'` — месяц прибытия.
# `'outcome_year'` — год прибытия.
import sqlite3
from flask import Flask
app = Flask(__name__)

@app.route('/<idx>')
def animals(idx):
    con = sqlite3.connect("animal.db")
    cur = con.cursor()
    sqlite_query = f"""
                select * from animals_fin 
                left join outcomes on outcomes.outcome_id = animals_fin.animal_id
                where animals_fin.id={idx}
    """

    cur.execute(sqlite_query)
    result = cur.fetchall()
    con.close()

    if len(result) == 1:
        line = result[0]
        result_dict = {
            'id': line[0],
            'animal_id': line[1],
            'type_id': line[2],
            'name': line[2],
            'breed_id': line[3],
            'date_of_birth': line[4],
            'outcome_id': line[5],
            'age_upon_outcome': line[6],
            'outcome_subtype': line[7],
            'outcome_type': line[8],
            'outcome_month': line[9],
            'outcome_year': line[10],

            }
    else:
        result_dict = {}
    return result_dict

app.run(debug=True)

