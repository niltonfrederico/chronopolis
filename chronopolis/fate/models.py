from decimal import Decimal
from typing import TYPE_CHECKING

from django.contrib.postgres.indexes import BTreeIndex
from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

from chronopolis.prometheus.enums import AccountType
from chronopolis.prometheus.enums import Category
from chronopolis.prometheus.enums import Direction
from chronopolis.prometheus.models import BaseModel


if TYPE_CHECKING:
    from chronopolis.prometheus.models import BooleanFieldType
    from chronopolis.prometheus.models import CharFieldType
    from chronopolis.prometheus.models import ChoiceStrFieldType
    from chronopolis.prometheus.models import DateTimeFieldType
    from chronopolis.prometheus.models import DecimalFieldType
    from chronopolis.prometheus.models import ForeignKeyType
    from chronopolis.prometheus.models import PositiveIntegerFieldType
    from chronopolis.prometheus.models import TextFieldType


class Account(BaseModel):
    name: CharFieldType = models.CharField(max_length=48)
    type: ChoiceStrFieldType[AccountType] = models.CharField(
        max_length=16, choices=AccountType.choices
    )
    balance: DecimalFieldType = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("0.00")
    )

    def __str__(self) -> str:
        return f"Account {self.name}({self.type})"


class Transaction(BaseModel):
    account: ForeignKeyType[Account] = models.ForeignKey(
        Account, on_delete=models.PROTECT, related_name="transactions"
    )
    direction: ChoiceStrFieldType[Direction] = models.CharField(
        max_length=8, choices=Direction.choices
    )
    category: ChoiceStrFieldType[Category] = models.CharField(
        max_length=16, choices=Category.choices
    )

    amount: DecimalFieldType = models.DecimalField(max_digits=10, decimal_places=2)
    description: TextFieldType = models.TextField(blank=True)

    paid_at: DateTimeFieldType = models.DateTimeField()
    due_at: DateTimeFieldType = models.DateTimeField()
    payment_planned_for: DateTimeFieldType = models.DateTimeField(blank=True, null=True)
    ignored: BooleanFieldType = models.BooleanField(default=False)
    is_installment: BooleanFieldType = models.BooleanField(default=False)
    installment_number: PositiveIntegerFieldType = models.PositiveIntegerField(
        blank=True, null=True
    )
    previous_installment: ForeignKeyType["Transaction"] = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="next_installment",
    )

    class Meta(TypedModelMeta):
        ordering = ("-due_at",)
        indexes = (
            BTreeIndex(fields=["account"]),
            BTreeIndex(fields=["direction"]),
            BTreeIndex(fields=["category"]),
            BTreeIndex(
                fields=["paid_at"],
                condition=models.Q(paid_at__isnull=True),
                name="unpaid_paid_at_idx",
            ),
        )

    def __str__(self) -> str:
        return f"Transaction {self.direction} {self.amount} on {self.account.name}"
