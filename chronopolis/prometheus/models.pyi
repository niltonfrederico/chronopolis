from datetime import datetime
from typing import Any

from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

class BaseModel(models.Model):
    created_at: datetime
    updated_at: datetime

    class Meta(TypedModelMeta):
        pass

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
