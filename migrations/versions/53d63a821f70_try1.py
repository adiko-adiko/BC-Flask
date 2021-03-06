"""try1

Revision ID: 53d63a821f70
Revises: 322e3354b8e2
Create Date: 2021-04-08 17:59:09.491302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53d63a821f70'
down_revision = '322e3354b8e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ListofPuppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('spots', sa.Integer(), nullable=True),
    sa.Column('robot', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ListofOwners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('puppy_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['puppy_id'], ['ListofPuppies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ListofOwners')
    op.drop_table('ListofPuppies')
    # ### end Alembic commands ###
