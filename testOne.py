#import psycopg2
from flask import Flask
from urllib.parse import urlparse
import feedparser
import os

app = Flask(__name__)

#postgresql-cubed-30564

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def index():
    """
    url = urlparse(os.environ["DATABASE_URL"])
    connStr = "host = {} port = {} dbname = {} user = {} password = {}".format(url.hostname, url.port, url.path[1:], url.username, url.password)
    #conn = psycopg2.connect("dbname=TestDb password=evdt1234 user=postgres")
    conn = psycopg2.connect(connStr)

    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS table1 (name TEXT, number REAL);")

    name = "gSheng0"
    number = 12232016

    cur.execute("INSERT INTO table1  (name, number) VALUES ('{}', {})".format(name, number))
    cur.execute("SELECT * FROM table1")

    data = cur.fetchall()
    conn.close()

    output = "{} {}".format(data[0][0], data[0][1])
    return output
    """
    return "George Sheng 12232016"


app.run()



