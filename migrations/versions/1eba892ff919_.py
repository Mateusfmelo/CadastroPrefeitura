"""empty message

Revision ID: 1eba892ff919
Revises: 
Create Date: 2022-11-19 12:43:21.420774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eba892ff919'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_prefeitura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=False),
    sa.Column('nomePrefeito', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome'),
    sa.UniqueConstraint('nomePrefeito')
    )
    op.create_table('tb_endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cep', sa.String(length=9), nullable=False),
    sa.Column('numero', sa.String(length=9), nullable=False),
    sa.Column('complemento', sa.String(), nullable=False),
    sa.Column('referencia', sa.String(), nullable=False),
    sa.Column('logradouro', sa.String(), nullable=False),
    sa.Column('prefeitura_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prefeitura_id'], ['tb_prefeitura.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_endereco')
    op.drop_table('tb_prefeitura')
    # ### end Alembic commands ###
