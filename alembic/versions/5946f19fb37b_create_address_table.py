"""Create address table

Revision ID: 5946f19fb37b
Revises: c69200d789d1
Create Date: 2023-07-10 20:56:53.262106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5946f19fb37b'
down_revision = 'c69200d789d1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('address1',sa.String(), nullable=False),
                    sa.Column('address2', sa.String(),nullable=False),
                    sa.Column('city',sa.String(),nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country',sa.String(),nullable=False),
                    sa.Column('postalcode',sa.String(),nullable=False))


def downgrade():
    op.drop_table('address')
