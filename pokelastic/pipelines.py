from scrapy.item import Item

from pokelastic.elasticsearch import Pokemon


class PokelasticPipeline:
    def process_item(self, item: Item, _) -> Item:
        pokemon = Pokemon(meta={"id": item["id"]}, **item)
        pokemon.save()
        return item
