"""create phone number for user col

Revision ID: c69200d789d1
Revises: 
Create Date: 2023-07-10 20:03:23.425813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c69200d789d1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users',sa.Column('phone_number', sa.String(),nullable=True))


def downgrade():
   op.drop_column('users','phone_number')
