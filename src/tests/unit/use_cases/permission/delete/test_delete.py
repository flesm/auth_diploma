from uuid import UUID

import pytest

from src.app.application.use_cases.permissions.delete.use_case import (
    DeletePermissionUseCase,
)
from src.app.application.use_cases.permissions.exceptions import (
    PermissionNotFoundException,
)


class TestDelete:

    async def test_case_1(
        self,
        delete_permission_uc: DeletePermissionUseCase,
        another_permission_id: UUID,
    ) -> None:
            result = await delete_permission_uc(permission_id=another_permission_id)

            assert result

    async def test_case_2(
        self,
        delete_permission_uc: DeletePermissionUseCase,
        foreign_permission_id: UUID,
    ) -> None:
            with pytest.raises(PermissionNotFoundException):
                await delete_permission_uc(permission_id=foreign_permission_id)
