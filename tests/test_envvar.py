import os
import unittest

from envvar import load, parse


class TestEnvvar(unittest.TestCase):
    def test_invalid_config(self) -> None:
        """test raises in invalid cases"""

        with self.assertRaises(FileExistsError):
            load("./file_does_not_exist")

    def test_valid_config(self) -> None:
        """test valid config"""

        config = """
        defaults:
            PORT: 4000
        required:
            - PORT
        local:
            DB: "pg"
        """

        p = parse(config, "local")

        assert len(p["required"]) == 1
        assert "PORT" in p["required"]

        assert len(p["defaults"].keys()) == 1
        assert "PORT" in p["defaults"].keys()
        assert p["defaults"].get("PORT") == "4000"

        assert len(p["local"].keys()) == 1
        assert "DB" in p["local"].keys()
        assert p["local"].get("DB") == "pg"

    def test_env_setter(self):
        """test if the env vars are being properly set"""

        assert os.environ.get("PORT") is None
        assert os.environ.get("DB_NAME") is None
        assert os.environ.get("HOST") is None

        load(os.getcwd() + "/examples/config.yaml", "local")

        assert os.environ.get("PORT") == "3000"
        assert os.environ.get("DB_NAME") == "local_db"
        assert os.environ.get("HOST") == "0.0.0.0"
