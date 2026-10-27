import unittest
from app import pagina_inicial


class TestAplicacao(unittest.TestCase):

    def test_pagina_inicial(self):
        return "Bem-vindo à DevFlow Solutions!"

if __name__ == "__main__":
    unittest.main()
