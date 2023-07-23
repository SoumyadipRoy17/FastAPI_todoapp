"""Create address_id to users

Revision ID: 1bbfe831eb42
Revises: 5946f19fb37b
Create Date: 2023-07-10 22:20:32.380436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bbfe831eb42'
down_revision = '5946f19fb37b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',sa.Column('address_id',sa.Integer(), nullable=True))

    op.create_foreign_key('address_users_fk', source_table="users",referent_table="address",
                          local_cols=['address_id'],remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users','address_id')
