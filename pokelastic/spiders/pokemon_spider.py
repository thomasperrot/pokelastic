import urllib
import urllib.parse
from datetime import datetime, timedelta
import re
from typing import Generator, Union

import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from pokelastic.items import Pokemon


class VideoSpider(scrapy.Spider):
    name = "pokemons"
    start_urls = ["https://pokemon.fandom.com/wiki/Bulbasaur"]

    def parse(self, response: HtmlResponse) -> Generator[Union[Pokemon, Request], None, None]:
        name = response.xpath("//h1[contains(@class, 'page-header__title')]/text()").get()
        types = list({e.get().split(" ")[0].lower() for e in response.xpath("//div[contains(@data-source, 'type')]//a[contains(@class, 'image')]/@title")})
        id_ = int(response.xpath("//div[contains(@data-source, 'ndex')]/text()").get())
        description = "\n".join(e.get() for e in response.xpath("//div[contains(@id, 'mw-content-text')]/p"))
        yield Pokemon(id=id_, name=name, types=types, description=description)

        next_url = response.xpath("//div[contains(@data-source, 'ndexnext')]/a/@href").get()
        yield response.follow(next_url, callback=self.parse)
