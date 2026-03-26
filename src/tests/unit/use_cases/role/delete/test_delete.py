from uuid import UUID

import pytest

from src.app.application.use_cases.roles.delete.controllers import (
    DeleteRoleUseCase,
)
from src.app.application.use_cases.roles.exceptions import (
    RoleNotFoundException,
)


class TestDelete:

    async def test_case_1(
        self,
        delete_role_uc: DeleteRoleUseCase,
        another_role_id: UUID,
    ) -> None:
            result = await delete_role_uc(role_id=another_role_id)

            assert result

    async def test_case_2(
        self,
        delete_role_uc: DeleteRoleUseCase,
        foreign_role_id: UUID,
    ) -> None:
            with pytest.raises(RoleNotFoundException):
                await delete_role_uc(role_id=foreign_role_id)
