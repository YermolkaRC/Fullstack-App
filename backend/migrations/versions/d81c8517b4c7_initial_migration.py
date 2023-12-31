"""Initial migration

Revision ID: d81c8517b4c7
Revises: 
Create Date: 2023-08-30 13:36:05.598389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd81c8517b4c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('imageUrl', sa.String(length=100), nullable=False),
    sa.Column('contractTypeId', sa.Integer(), nullable=False),
    sa.Column('contractSignedOn', sa.DateTime(), nullable=False),
    sa.Column('budget', sa.Integer(), nullable=False),
    sa.Column('isActive', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###
