"""create dados_gerais_populacao_populacao table

Revision ID: 1ec28590e701
Revises: 
Create Date: 2022-12-04 11:56:24.462756

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '1ec28590e701'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'dados_gerais_populacao_populacao',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('codigo_ibge', sa.Integer, nullable=False),
        sa.Column('nome_regiao', sa.String(100), nullable=False),
        sa.Column('tipo_regiao', sa.String(70), nullable=False),
        sa.Column('valor', sa.Float, nullable=False),
        sa.Column('ano', sa.Integer, nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('dados_gerais_populacao_populacao')
