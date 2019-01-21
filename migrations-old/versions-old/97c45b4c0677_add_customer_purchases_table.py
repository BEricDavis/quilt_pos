"""add customer_purchases table

Revision ID: 97c45b4c0677
Revises: d8491d765e07
Create Date: 2019-01-19 16:52:38.728125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97c45b4c0677'
down_revision = 'd8491d765e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer_purchases',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchase.id'], ),
    sa.PrimaryKeyConstraint('customer_id', 'purchase_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer_purchases')
    # ### end Alembic commands ###