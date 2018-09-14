"""blog table

Revision ID: 86665c83b5df
Revises: 62c207cf1ff3
Create Date: 2018-09-14 15:53:07.814028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86665c83b5df'
down_revision = '62c207cf1ff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hash_pass', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('blog_pic_path', sa.String(), nullable=False),
    sa.Column('contributor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contributor_id'], ['contributor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Contributor')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Contributor',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Contributor_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('hash_pass', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Contributor_pkey'),
    sa.UniqueConstraint('email', name='Contributor_email_key')
    )
    op.drop_table('blog')
    op.drop_table('contributor')
    # ### end Alembic commands ###
