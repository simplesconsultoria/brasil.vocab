# -*- coding:utf-8 -*-
import unittest


class CidadesUnitTests(unittest.TestCase):

    def test_cidades_por_estado(self):
        from brasil.vocab.geo.cidade import cidadesPorEstado
        self.assertEqual(len(cidadesPorEstado.keys()), 27)
        self.assertEqual(len(cidadesPorEstado['AC']), 22)
        self.assertEqual(cidadesPorEstado['AC'][-1][0], 1200708)
        self.assertEqual(cidadesPorEstado['AC'][-1][1], 'Xapuri')

    def test_cidades(self):
        from brasil.vocab.geo.cidade import cidades
        self.assertEqual(len(cidades), 5565)
        self.assertEqual(cidades[0][0], 5200050)
        self.assertEqual(cidades[0][1], u"Abadia de Goiás")
        self.assertEqual(cidades[0][2], u'GO')
        self.assertEqual(cidades[0][3], "abadia de goias")


class UFsUnitTests(unittest.TestCase):

    def test_uf(self):
        from brasil.vocab.geo.uf import uf
        self.assertEqual(len(uf), 27)
        self.assertEqual(uf[-1][0], u'TO')
        self.assertEqual(uf[-1][1], u'Tocantins')


class PaisUnitTests(unittest.TestCase):

    def test_paises(self):
        from brasil.vocab.geo.pais import paises
        self.assertEqual(len(paises), 244)
        self.assertEqual(paises[0][0], u'BR')
        self.assertEqual(paises[0][1], u'Brasil')
        self.assertEqual(paises[-1][0], u'ZW')
        self.assertEqual(paises[-1][1], u'Zimbabwe')
