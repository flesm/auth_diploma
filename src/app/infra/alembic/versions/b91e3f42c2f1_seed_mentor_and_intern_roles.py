"""seed mentor and intern roles

Revision ID: b91e3f42c2f1
Revises: a8d5e7f3be0b
Create Date: 2026-03-21 23:15:00
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "b91e3f42c2f1"
down_revision: Union[str, None] = "a8d5e7f3be0b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.execute(
        sa.text(
            """
            INSERT INTO roles (id, name, description)
            SELECT uuid_generate_v4(), :name, :description
            WHERE NOT EXISTS (
                SELECT 1 FROM roles WHERE name = :name
            )
            """
        ).bindparams(name="mentor", description="Mentor role")
    )
    op.execute(
        sa.text(
            """
            INSERT INTO roles (id, name, description)
            SELECT uuid_generate_v4(), :name, :description
            WHERE NOT EXISTS (
                SELECT 1 FROM roles WHERE name = :name
            )
            """
        ).bindparams(name="intern", description="Intern role")
    )


def downgrade() -> None:
    op.execute(sa.text("DELETE FROM roles WHERE name IN ('mentor', 'intern')"))
