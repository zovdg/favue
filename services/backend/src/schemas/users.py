from tortoise.contrib.pydantic import pydantic_model_creator

from ..database.models import Users


UserInSchema = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=("password", "created_at", "updated_at")
)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=("created_at", "updated_at")
)
