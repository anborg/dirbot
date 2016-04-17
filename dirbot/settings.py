# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1}

ITEM_PIPELINES = [
    'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline',
]

ELASTICSEARCH_SERVERS = ['http://192.168.99.100:9200']
ELASTICSEARCH_INDEX = 'scrapy'
ELASTICSEARCH_TYPE = 'items'
ELASTICSEARCH_UNIQ_KEY = 'url'
