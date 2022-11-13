import unittest
from bolos import *

class Test(unittest.TestCase):
    
    def test_numero_jugadas(self):
        self.assertEqual(jugadas, 10)
    
    def test_oportunidades(self):
        self.assertEqual(oportunidades, 2)   
    
    def test_puntuacion_total(self):
        self.assertEqual(puntuacion(), 8)
    
    def test_suma_Puntuacion(self):
        puntuacionPrimerTiro = 5
        puntuacionSegundoTiro = 3
        puntuacionSuma = puntuacionPrimerTiro + puntuacionSegundoTiro
        self.assertEqual(puntuacion(), puntuacionSuma)
    
    
if __name__ == "__main__":
    unittest.main()