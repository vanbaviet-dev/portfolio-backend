"""Add pos field to Word

Revision ID: b21f618fbedd
Revises: 
Create Date: 2025-06-14 16:11:40.133777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b21f618fbedd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('word', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pos', sa.String(length=100), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('word', schema=None) as batch_op:
        batch_op.drop_column('pos')

    # ### end Alembic commands ###
