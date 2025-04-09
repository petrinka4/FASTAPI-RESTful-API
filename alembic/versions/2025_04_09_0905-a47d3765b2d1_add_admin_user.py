"""add_admin_user

Revision ID: a47d3765b2d1
Revises: 1e99b0e6cff3
Create Date: 2025-04-09 09:05:28.538640

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a47d3765b2d1"
down_revision: Union[str, None] = "1e99b0e6cff3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    users_table = sa.table(
        'users',
        sa.column('id', sa.Integer),
        sa.column('username', sa.String),
        sa.column('password', sa.String),
        sa.column('role_id', sa.Integer),
        sa.column('active', sa.Boolean)
    )

    op.bulk_insert(
        users_table,
        [
            {
                "id": 1,
                "username": "admin",
                "password": "$2b$12$YvBLW1fnhABirucMNbxV6OmO4eV1y1pw3EX1Q3KKNNsSe7.EZKxH6", 
                "role_id": 1,
                "active": True
            }
        ]
    )


def downgrade():
    op.execute("DELETE FROM users WHERE id IN (1)")