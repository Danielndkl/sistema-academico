import unittest

from calificaciones import (
    calcular_promedio,
    determinar_estado,
    registrar_calificacion
)


class TestCalificaciones(unittest.TestCase):

    # Caso 1: comprobar el promedio
    def test_calcular_promedio(self):
        resultado = calcular_promedio(80, 70, 90)
        self.assertEqual(resultado, 80)

    # Caso 2: comprobar que el estudiante aprueba
    def test_estudiante_aprobado(self):
        resultado = registrar_calificacion(80, 70, 90)
        self.assertEqual(resultado["estado"], "Aprobado")

    # Caso 3: comprobar que una nota invalida genera un error
    def test_nota_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            calcular_promedio(80, 120, 90)


if __name__ == "__main__":
    unittest.main()
