"""empty message

Revision ID: d8266fa0a9c3
Revises: 
Create Date: 2021-08-20 23:44:01.142205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8266fa0a9c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('category_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('category_calendar',
    sa.Column('category_calendar_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('category_calendar_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('fullname', sa.String(length=200), nullable=True),
    sa.Column('about', sa.Text(), nullable=True),
    sa.Column('fb_link', sa.String(length=100), nullable=True),
    sa.Column('tw_link', sa.String(length=100), nullable=True),
    sa.Column('git_link', sa.String(length=100), nullable=True),
    sa.Column('web_link', sa.String(length=100), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('image_file', sa.String(length=200), nullable=False),
    sa.Column('roles', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roles'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('calendar',
    sa.Column('calendar_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('start', sa.String(length=20), nullable=False),
    sa.Column('end', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category_calendar.category_calendar_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('calendar_id')
    )
    op.create_table('code',
    sa.Column('code_id', sa.Integer(), nullable=False),
    sa.Column('source', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('code_id')
    )
    op.create_table('note',
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=False),
    sa.Column('note', sa.String(length=200000), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('note_id')
    )
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('brief', sa.String(length=300), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('image_cover', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tags', sa.String(length=200), nullable=True),
    sa.Column('like', sa.Integer(), nullable=True),
    sa.Column('dislike', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.category_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('post_id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('comments',
    sa.Column('commnet_id', sa.Integer(), nullable=False),
    sa.Column('like', sa.Integer(), nullable=True),
    sa.Column('dislike', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date_comment', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('commnet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('roles_users')
    op.drop_table('post')
    op.drop_table('note')
    op.drop_table('code')
    op.drop_table('calendar')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('category_calendar')
    op.drop_table('category')
    # ### end Alembic commands ###
