"""customers table

Revision ID: 0cc82c42cea5
Revises: 
Create Date: 2019-01-13 20:39:27.599104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cc82c42cea5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('street1', sa.String(length=64), nullable=True),
    sa.Column('street2', sa.String(length=64), nullable=True),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.Column('state', sa.String(length=6), nullable=True),
    sa.Column('zip', sa.String(length=16), nullable=True),
    sa.Column('country', sa.String(length=64), nullable=True),
    sa.Column('last_purchase', sa.DateTime(), nullable=True),
    sa.Column('reward_points', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_index(op.f('ix_customers_city'), 'customers', ['city'], unique=False)
    op.create_index(op.f('ix_customers_country'), 'customers', ['country'], unique=False)
    op.create_index(op.f('ix_customers_email'), 'customers', ['email'], unique=True)
    op.create_index(op.f('ix_customers_first_name'), 'customers', ['first_name'], unique=False)
    op.create_index(op.f('ix_customers_last_name'), 'customers', ['last_name'], unique=False)
    op.create_index(op.f('ix_customers_state'), 'customers', ['state'], unique=False)
    op.create_index(op.f('ix_customers_street1'), 'customers', ['street1'], unique=False)
    op.create_index(op.f('ix_customers_street2'), 'customers', ['street2'], unique=False)
    op.create_index(op.f('ix_customers_zip'), 'customers', ['zip'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customers_zip'), table_name='customers')
    op.drop_index(op.f('ix_customers_street2'), table_name='customers')
    op.drop_index(op.f('ix_customers_street1'), table_name='customers')
    op.drop_index(op.f('ix_customers_state'), table_name='customers')
    op.drop_index(op.f('ix_customers_last_name'), table_name='customers')
    op.drop_index(op.f('ix_customers_first_name'), table_name='customers')
    op.drop_index(op.f('ix_customers_email'), table_name='customers')
    op.drop_index(op.f('ix_customers_country'), table_name='customers')
    op.drop_index(op.f('ix_customers_city'), table_name='customers')
    op.drop_table('customers')
    # ### end Alembic commands ###