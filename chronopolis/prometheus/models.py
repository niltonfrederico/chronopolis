import uuid
from decimal import Decimal
from typing import TYPE_CHECKING

from django.db import models
from django_stubs_ext.db.models import TypedModelMeta


if TYPE_CHECKING:
    from datetime import datetime

type BooleanFieldType = models.BooleanField[bool, bool]
type CharFieldType = models.CharField[str, str]
type ChoiceStrFieldType[TextChoices] = models.CharField[TextChoices | str, TextChoices]
type DateTimeFieldType = models.DateTimeField[str | datetime, datetime]
type DecimalFieldType = models.DecimalField[str | int | float | Decimal, Decimal]
type ForeignKeyType[RelatedModel] = models.ForeignKey[RelatedModel, RelatedModel]
type TextFieldType = models.TextField[str, str]
type UUIDFieldType = models.UUIDField[str | uuid.UUID, uuid.UUID]
type PositiveIntegerFieldType = models.PositiveIntegerField[int, int]


class BaseModel(models.Model):
    id: UUIDFieldType = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    created_at: DateTimeFieldType = models.DateTimeField(
        auto_now_add=True, editable=False
    )
    updated_at: DateTimeFieldType = models.DateTimeField(auto_now=True, editable=False)

    class Meta(TypedModelMeta):
        abstract = True
