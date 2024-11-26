"""hafsdkjfhasdkjf

Revision ID: 8aa5e6f89fee
Revises: 50fe8cd8d030
Create Date: 2024-11-25 21:16:16.265724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aa5e6f89fee'
down_revision = '50fe8cd8d030'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.drop_column('tipo_cuenta')

    with op.batch_alter_table('historial_movimientos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipo_cuenta', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('historial_movimientos', schema=None) as batch_op:
        batch_op.drop_column('tipo_cuenta')

    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tipo_cuenta', sa.VARCHAR(length=50), nullable=True))

    # ### end Alembic commands ###
