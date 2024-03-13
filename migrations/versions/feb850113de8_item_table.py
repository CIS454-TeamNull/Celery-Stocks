"""item table

Revision ID: feb850113de8
Revises: 4e0a85a79357
Create Date: 2024-03-13 11:13:33.115231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feb850113de8'
down_revision = '4e0a85a79357'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('supply', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_item_name'), ['name'], unique=True)
        batch_op.create_index(batch_op.f('ix_item_supply'), ['supply'], unique=False)
        batch_op.create_index(batch_op.f('ix_item_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_item_timestamp'))
        batch_op.drop_index(batch_op.f('ix_item_supply'))
        batch_op.drop_index(batch_op.f('ix_item_name'))

    op.drop_table('item')
    # ### end Alembic commands ###
