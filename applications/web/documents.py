from django_elasticsearch_dsl import DocType, Index, fields
from elasticsearch_dsl import analyzer, tokenizer

from applications.web.models import Point

# Name of the Elasticsearch index
point = Index('point')

# See Elasticsearch Indices API reference for available settings
point.settings(
    number_of_shards=1,
    number_of_replicas=0
)

address_analyzer = analyzer(
    'address_analyzer',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=2, max_gram=4),
    filter=['lowercase']
)


@point.doc_type
class PointDocument(DocType):
    # address = fields.TextField(
    #     analyzer=address_analyzer,
    #     fields={'raw': fields.KeywordField()}
    # )
    location = fields.GeoPointField()

    def prepare_location(self, instance):
        return {"lat": instance.latitude, "lon": instance.longitude}

    class Meta:
        model = Point  # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'store_type',
            'identity',
            'province',
            'city',
            'district',
            'name',
            'address',
            'linkman',
            'telephone',
            'service_time',
        ]

        ignore_signals = False
        auto_refresh = True
