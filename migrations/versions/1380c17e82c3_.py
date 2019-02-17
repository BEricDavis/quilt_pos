"""empty message

Revision ID: 1380c17e82c3
Revises: dfb7dbd963b8
Create Date: 2019-02-03 10:30:37.422818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1380c17e82c3'
down_revision = 'dfb7dbd963b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchase_items',
    sa.Column('purchase_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchase.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchase_items')
    # ### end Alembic commands ###
