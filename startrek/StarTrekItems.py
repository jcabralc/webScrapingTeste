from scrapy.item import Item, Field

class StarTrekItem(Item):
    title = Field()
    url = Field()
