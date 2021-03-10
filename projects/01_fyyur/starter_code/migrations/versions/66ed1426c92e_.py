"""empty message

Revision ID: 66ed1426c92e
Revises: f0802a342100
Create Date: 2021-03-10 18:15:43.291682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66ed1426c92e'
down_revision = 'f0802a342100'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Genre', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Genre', 'Venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Genre', type_='foreignkey')
    op.drop_column('Genre', 'venue_id')
    # ### end Alembic commands ###