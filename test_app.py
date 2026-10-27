import unittest
from app import pagina_inicial


class TestAplicacao(unittest.TestCase):

    def test_pagina_inicial(self):
        resultado = pagina_inicial()

        self.assertEqual(
            resultado,
            "Bem-vindo à DevFlow Solutions!"
        )


if __name__ == "__main__":
    unittest.main()