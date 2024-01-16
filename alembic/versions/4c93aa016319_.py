"""empty message

Revision ID: 4c93aa016319
Revises: 4b6e7fdcfe14
Create Date: 2024-01-16 06:11:50.498359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c93aa016319'
down_revision: Union[str, None] = '4b6e7fdcfe14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_authors_id', table_name='authors')
    op.drop_table('authors')
    op.drop_index('ix_books_id', table_name='books')
    op.drop_index('ix_books_name', table_name='books')
    op.drop_table('books')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='books_pkey')
    )
    op.create_index('ix_books_name', 'books', ['name'], unique=True)
    op.create_index('ix_books_id', 'books', ['id'], unique=False)
    op.create_table('authors',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='authors_pkey')
    )
    op.create_index('ix_authors_id', 'authors', ['id'], unique=False)
    # ### end Alembic commands ###
