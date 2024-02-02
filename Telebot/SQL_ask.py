import psycopg2

from config_reader import config

conn = psycopg2.connect(dbname=config.dbname.get_secret_value(), user=config.user.get_secret_value(),
                        password=config.password.get_secret_value(), host=config.host.get_secret_value(),
                        port=config.port.get_secret_value())


def check_for_new_record():
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM main_form_articles WHERE is_new = true")

    last_updated = cursor.fetchone()[0]

    if last_updated > 0:
        return True
    else:
        return False


def send_for_new_date():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM main_form_articles WHERE is_new = true")

    last_updated = cursor.fetchall()

    cursor.execute('UPDATE main_form_articles SET is_new = false WHERE is_new = true')

    conn.commit()

    buff = ''

    for k in last_updated:
        buff += f"Номер заявки: {k[0]}\nЗаявитель: {k[1]}\nТекст заявки: {k[8]}\n\n"
    if len(buff) > 0:
        return buff
    else:
        return None
