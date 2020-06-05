from elasticsearch_dsl import Document, Text, Keyword, Integer, analyzer
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])

html_strip = analyzer(
    "html_strip",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


class Pokemon(Document):
    id = Integer()
    name = Keyword()
    types = Keyword()
    description = Text(analyzer=html_strip)

    class Index:
        name = "pokemons"
        settings = {
            "number_of_shards": 1,
        }


Pokemon.init()
