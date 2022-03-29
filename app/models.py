from sqlalchemy import Column, ForeignKey, Boolean, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

from sqlalchemy_serializer import SerializerMixin


class Roles(Base, SerializerMixin):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    serialize_rules = ('-users.role',)

    users = relationship("Users", back_populates="roles")


class Users(Base, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Null", nullable=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Roles", back_populates="users")


class Applicants(Base, SerializerMixin):
    __tablename__ = 'applicants'

    id = Column(Integer, primary_key=True, index=True)


# ----------------------------------------------------------------------------
# Sample:
#
# class Dashboard(Base, SerializerMixin):
#     __tablename__ = 'dashboards'
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#
#     serialize_rules = ('-tasks.dashboard',)
#
#     tasks = relationship("Task", back_populates="dashboard")
#
#
# class Task(Base, SerializerMixin):
#     __tablename__ = 'tasks'
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     is_active = Column(Boolean, default=True)
#     dashboard_id = Column(Integer, ForeignKey("dashboards.id"))
#
#     dashboard = relationship("Dashboard", back_populates="tasks")
#
# -----------------------------------------------------
