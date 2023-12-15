"""empty message

Revision ID: d39c5439d56d
Revises: 26c5ee45d80a
Create Date: 2023-12-13 17:18:57.734740

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd39c5439d56d'
down_revision = '26c5ee45d80a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('interest_info', schema=None) as batch_op:
        batch_op.drop_constraint('interest_info_ibfk_1', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('interest_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('interest_info_ibfk_1', 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###
