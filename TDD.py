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
    
    def test_puntuación_total_partida_nula(self):
        partida = ([0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0])
        suma_partida = sum(list(map(sum, partida)))
        self.assertEqual(valorPartida(), suma_partida)
        
    def test_puntuación_total_partida_1(self):
        partida = ([5,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0])
        suma_partida = sum(list(map(sum, partida)))
        self.assertEqual(valorPartida(), suma_partida)
        
if __name__ == "__main__":
    unittest.main()