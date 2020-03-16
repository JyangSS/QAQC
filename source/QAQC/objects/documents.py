from django_elasticsearch_dsl import (
    Document,
    Index,
)
from .models import *

posts = Index('posts')


@posts.document
class ProjectDocument(Document):
    class Django:
        model = Project
        fields = [
            'company',
            'project_description',
            'project_short_form',
        ]
