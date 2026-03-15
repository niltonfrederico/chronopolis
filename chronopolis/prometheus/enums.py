from enum import auto

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class LowerCaseTextChoices(TextChoices):
    @staticmethod
    def _generate_next_value_(
        name: str, start: int, count: int, last_values: list[str]
    ) -> str:
        return name.lower()


class Direction(LowerCaseTextChoices):
    INCOME = auto(), _("Income")
    OUTCOME = auto(), _("Outcome")


class Categories(LowerCaseTextChoices):
    # Food -> Groceries, Restaurants, Cafes
    FOOD = auto(), _("Food")
    # Transport -> Public Transport, Uber, Gas
    TRANSPORT = auto(), _("Transport")
    # Entertainment -> Movies, Concerts, Pubs
    ENTERTAINMENT = auto(), _("Entertainment")
    # Health -> Doctor, Pharmacy, Gym, Psychologist
    HEALTH = auto(), _("Health")
    # Education -> Books, Courses, Tuition
    EDUCATION = auto(), _("Education")
    # Pet -> Food, Vet, Toys
    PET = auto(), _("Pet")
    # Self Care -> Haircut, Skincare, Clothing
    SELF_CARE = auto(), _("Self Care")
    # Home -> Rent, Mortgage, Furniture, Repairs, Appliances
    HOME = auto(), _("Home")
    # Debt -> Unpaid things
    DEBT = auto(), _("Debt")
    # Loan -> Student, Car, Personal, Friends
    LOAN = auto(), _("Loan")
    # Work -> Salary, freelance, tools, software
    WORK = auto(), _("Work")
    # Utilities -> Electricity, Water, Internet, Phone
    UTILITIES = auto(), _("Utilities")
    # Other -> Miscellaneous, Uncategorized
    OTHER = auto(), _("Other")
