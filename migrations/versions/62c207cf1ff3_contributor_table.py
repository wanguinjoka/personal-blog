"""Contributor table

Revision ID: 62c207cf1ff3
Revises: cdd8cee81fdd
Create Date: 2018-09-14 14:53:13.203567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62c207cf1ff3'
down_revision = 'cdd8cee81fdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hash_pass', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.alter_column('Follower', 'hash_pass',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_constraint('Follower_name_key', 'Follower', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Follower_name_key', 'Follower', ['name'])
    op.alter_column('Follower', 'hash_pass',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_table('Contributor')
    # ### end Alembic commands ###