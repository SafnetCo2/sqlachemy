"""Rename email to title

Revision ID: 323f480fb845
Revises: d0685015ee72
Create Date: 2024-05-28 22:41:40.837201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '323f480fb845'
down_revision: Union[str, None] = 'd0685015ee72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
