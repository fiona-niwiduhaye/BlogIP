"""Fourth  Migration

Revision ID: 32fb6f080dc0
Revises: 3ab7ccf78df7
Create Date: 2018-09-14 14:22:45.827749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32fb6f080dc0'
down_revision = '3ab7ccf78df7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('content', sa.String(length=4000), nullable=False))
    op.add_column('comments', sa.Column('dislikes', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('likes', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('time', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'time')
    op.drop_column('comments', 'likes')
    op.drop_column('comments', 'dislikes')
    op.drop_column('comments', 'content')
    # ### end Alembic commands ###
