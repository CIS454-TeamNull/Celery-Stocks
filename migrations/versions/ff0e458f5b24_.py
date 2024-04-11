"""empty message

Revision ID: ff0e458f5b24
Revises: 6af47405291b
Create Date: 2024-03-13 21:47:24.780904

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ff0e458f5b24"
down_revision = "6af47405291b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("account_type", sa.String(length=64), nullable=True)
        )
        batch_op.add_column(sa.Column("last_seen", sa.DateTime(), nullable=True))
        batch_op.create_index(
            batch_op.f("ix_user_account_type"), ["account_type"], unique=False
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_user_account_type"))
        batch_op.drop_column("last_seen")
        batch_op.drop_column("account_type")

    # ### end Alembic commands ###