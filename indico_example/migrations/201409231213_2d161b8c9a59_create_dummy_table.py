"""Create dummy table

Revision ID: 2d161b8c9a59
Revises: None
Create Date: 2014-09-23 12:13:17.697482
"""

import sqlalchemy as sa
from alembic import op

from sqlalchemy.sql.ddl import CreateSchema, DropSchema


# revision identifiers, used by Alembic.
revision = '2d161b8c9a59'
down_revision = None


def upgrade():
    op.execute(CreateSchema('plugin_example'))
    op.create_table('foo',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('bar', sa.String(), nullable=True),
                    sa.Column('location_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['location_id'], ['roombooking.locations.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    schema='plugin_example')


def downgrade():
    op.drop_table('foo', schema='plugin_example')
    op.execute(DropSchema('plugin_example'))
