"""adding seeking talent

Revision ID: 3b03f95f40f8
Revises: c93fba2ae6b4
Create Date: 2020-09-18 21:12:56.714904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b03f95f40f8'
down_revision = 'c93fba2ae6b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'seeking_talent')
    # ### end Alembic commands ###