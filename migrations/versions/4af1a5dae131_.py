"""empty message

Revision ID: 4af1a5dae131
Revises: 
Create Date: 2022-12-19 18:34:22.756452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4af1a5dae131'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_pessoa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('senha', sa.String(length=6), nullable=False),
    sa.Column('telefone', sa.String(length=11), nullable=True),
    sa.Column('nascimento', sa.Date(), nullable=True),
    sa.Column('tipo_pessoa', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tb_uf',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('sigla', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_cidade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('sigla', sa.String(length=3), nullable=False),
    sa.Column('uf_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uf_id'], ['tb_uf.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_prefeito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['tb_pessoa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cep', sa.String(length=8), nullable=False),
    sa.Column('numero', sa.String(length=9), nullable=False),
    sa.Column('complemento', sa.String(), nullable=False),
    sa.Column('referencia', sa.String(), nullable=False),
    sa.Column('logradouro', sa.String(), nullable=False),
    sa.Column('pessoa_id', sa.Integer(), nullable=True),
    sa.Column('cidade_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cidade_id'], ['tb_cidade.id'], ),
    sa.ForeignKeyConstraint(['pessoa_id'], ['tb_pessoa.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_prefeitura',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('secretarios', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('telefone', sa.String(length=100), nullable=False),
    sa.Column('prefeito_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prefeito_id'], ['tb_prefeito.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('secretarios'),
    sa.UniqueConstraint('telefone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_prefeitura')
    op.drop_table('tb_endereco')
    op.drop_table('tb_prefeito')
    op.drop_table('tb_cidade')
    op.drop_table('tb_uf')
    op.drop_table('tb_pessoa')
    # ### end Alembic commands ###