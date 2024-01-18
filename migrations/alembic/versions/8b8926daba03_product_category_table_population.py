"""Product category table population

Revision ID: 8b8926daba03
Revises: 9a009c50a0d9
Create Date: 2024-01-17 20:36:11.237642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b8926daba03'
down_revision: Union[str, None] = '9a009c50a0d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        INSERT INTO product_category 
            VALUES
            ('Sobremesa',1,now(),now()),
            ('Lanche',2,now(),now()),
            ('Bebida',3,now(),now()),
            ('Acompanhamento',4,now(),now())
    """)


def downgrade() -> None:
    op.execute("""
        DELETE FROM product_category
    """)
