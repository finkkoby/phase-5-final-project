"""initial revision

Revision ID: e708dcfbe1ba
Revises: 
Create Date: 2024-05-20 14:35:41.297185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e708dcfbe1ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('youtube_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_recents_user_id_users')),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], name=op.f('fk_recents_video_id_videos')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.String(length=5), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], name=op.f('fk_rooms_video_id_videos')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code')
    )
    op.create_table('guests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name=op.f('fk_guests_room_id_rooms')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('joins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('host', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], name=op.f('fk_joins_room_id_rooms')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_joins_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('joins')
    op.drop_table('guests')
    op.drop_table('rooms')
    op.drop_table('recents')
    op.drop_table('videos')
    op.drop_table('users')
    # ### end Alembic commands ###
