# Stubs for prov.serializers (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from prov import Error
from typing import Any, Optional

class Serializer:
    document: Any = ...
    def __init__(self, document: Optional[Any] = ...) -> None: ...
    def serialize(self, stream, **kwargs): ...
    def deserialize(self, stream, **kwargs): ...

class DoNotExist(Error): ...

class Registry:
    serializers: Any = ...
    @staticmethod
    def load_serializers(): ...

def get(format_name): ...
