"""engine to car? foreign key add

Revision ID: 3998df9331f3
Revises: d5663a3e6f56
Create Date: 2025-03-05 03:53:19.507199

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3998df9331f3"
down_revision: Union[str, None] = "d5663a3e6f56"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "engine",
        sa.Column("engine_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_engine_engine_name"), "engine", ["engine_name"], unique=True
    )
    op.create_table(
        "order",
        sa.Column("customer", sa.String(), nullable=False),
        sa.Column("phone", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "salone_member",
        sa.Column("salone_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_salone_member_salone_name"),
        "salone_member",
        ["salone_name"],
        unique=True,
    )
    op.create_table(
        "salone_option",
        sa.Column("salone_option_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_salone_option_salone_option_name"),
        "salone_option",
        ["salone_option_name"],
        unique=True,
    )
    op.create_table(
        "service",
        sa.Column("service_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_service_service_name"),
        "service",
        ["service_name"],
        unique=True,
    )
    op.create_table(
        "shassi",
        sa.Column("shassi_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_shassi_shassi_name"), "shassi", ["shassi_name"], unique=True
    )
    op.create_table(
        "zip",
        sa.Column("zip_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_zip_zip_name"), "zip", ["zip_name"], unique=True)
    op.create_table(
        "car",
        sa.Column("car_name", sa.String(), nullable=False),
        sa.Column("base_price", sa.Integer(), nullable=False),
        sa.Column("engine_id", sa.Integer(), nullable=False),
        sa.Column("salone_member", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["engine_id"],
            ["engine.id"],
        ),
        sa.ForeignKeyConstraint(
            ["salone_member"],
            ["salone_member.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_car_car_name"), "car", ["car_name"], unique=True)
    op.create_table(
        "saloneoption_car_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("salone_option_id", sa.Integer(), nullable=False),
        sa.Column("car_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["car_id"],
            ["car.id"],
        ),
        sa.ForeignKeyConstraint(
            ["salone_option_id"],
            ["salone_option.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "service_car_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("service_id", sa.Integer(), nullable=False),
        sa.Column("car_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["car_id"],
            ["car.id"],
        ),
        sa.ForeignKeyConstraint(
            ["service_id"],
            ["service.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "shassi_car_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("shassi_id", sa.Integer(), nullable=False),
        sa.Column("car_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["car_id"],
            ["car.id"],
        ),
        sa.ForeignKeyConstraint(
            ["shassi_id"],
            ["shassi.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "zip_car_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("zip_id", sa.Integer(), nullable=False),
        sa.Column("car_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["car_id"],
            ["car.id"],
        ),
        sa.ForeignKeyConstraint(
            ["zip_id"],
            ["zip.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("zip_car_association")
    op.drop_table("shassi_car_association")
    op.drop_table("service_car_association")
    op.drop_table("saloneoption_car_association")
    op.drop_index(op.f("ix_car_car_name"), table_name="car")
    op.drop_table("car")
    op.drop_index(op.f("ix_zip_zip_name"), table_name="zip")
    op.drop_table("zip")
    op.drop_index(op.f("ix_shassi_shassi_name"), table_name="shassi")
    op.drop_table("shassi")
    op.drop_index(op.f("ix_service_service_name"), table_name="service")
    op.drop_table("service")
    op.drop_index(
        op.f("ix_salone_option_salone_option_name"), table_name="salone_option"
    )
    op.drop_table("salone_option")
    op.drop_index(
        op.f("ix_salone_member_salone_name"), table_name="salone_member"
    )
    op.drop_table("salone_member")
    op.drop_table("order")
    op.drop_index(op.f("ix_engine_engine_name"), table_name="engine")
    op.drop_table("engine")
    # ### end Alembic commands ###
