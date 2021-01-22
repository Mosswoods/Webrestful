"""empty message

Revision ID: bc4dbd7e7eb6
Revises: c1e678f1a7d4
Create Date: 2020-12-31 20:13:23.961916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc4dbd7e7eb6'
down_revision = 'c1e678f1a7d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'gse', ['GSE_num'])
    op.create_foreign_key(None, 'gsm', 'gse', ['GSE_num'], ['GSE_num'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gsm', type_='foreignkey')
    op.drop_constraint(None, 'gse', type_='unique')
    # ### end Alembic commands ###