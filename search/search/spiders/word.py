import pandas as pd
import scrapy


url = "https://vplates.com.au/vplatesapi/checkcombo?vehicleType=car&combination={}"


class WordSpider(scrapy.Spider):
    name = "word"

    def start_requests(self):
        df = pd.read_csv("data/input.csv")
        for i, word in enumerate(df["search"].tolist()):
            yield scrapy.Request(
                url=url.format(word),
                callback=self.parse,
                cb_kwargs={"lookup": word},
            )

    def parse(self, response, lookup):
        data = response.json()
        success = data.get("success")
        yield {"Word": lookup, "Available": "Yes" if success else "Not"}
