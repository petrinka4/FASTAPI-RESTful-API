"""add_default_roles

Revision ID: 1e99b0e6cff3
Revises: f06e14567655
Create Date: 2025-04-08 11:29:52.035303

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1e99b0e6cff3"
down_revision: Union[str, None] = "f06e14567655"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    roles_table = sa.table(
        'roles',
        sa.column('id', sa.Integer),
        sa.column('name', sa.String)
    )

    op.bulk_insert(
        roles_table,
        [
            {"id": 1, "name": "admin"},
            {"id": 2, "name": "editor"},
            {"id": 3, "name": "user"},
        ]
    )


def downgrade():
    op.execute("DELETE FROM roles WHERE id IN (1, 2, 3)")