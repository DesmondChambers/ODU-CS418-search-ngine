from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from .models import Search


@registry.register_document
class searchDocument(Document):
    class Index:
        name = 'searchx'
        settings = {
            'number_of_shards': 1, 
            'number_of_replicas': 0
        }
    class Django:
        model = Search

        fields = [
            'id',
            'contributor_author',
            'description_abstract',
            'identifier_uri',
            'slug',
        ]