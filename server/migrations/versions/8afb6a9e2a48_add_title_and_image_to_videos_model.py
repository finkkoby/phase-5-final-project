"""add title and image to videos model

Revision ID: 8afb6a9e2a48
Revises: 8d078e51eb36
Create Date: 2024-05-23 15:06:07.550211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8afb6a9e2a48'
down_revision = '8d078e51eb36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videos', schema=None) as batch_op:
        batch_op.drop_column('url')

    # ### end Alembic commands ###