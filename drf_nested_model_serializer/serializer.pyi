from functools import cached_property as cached_property
from rest_framework.serializers import ModelSerializer

INCLUDE_FIELD: str
EXCLUDE_FIELD: str
ALL_FIELDS: str

class NestedModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs) -> None: ...
    def create(self, validated_data): ...
    def update(self, instance, validated_data): ...
