import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


@pytest.mark.usefixtures("login")
class loginTest:
    pass
