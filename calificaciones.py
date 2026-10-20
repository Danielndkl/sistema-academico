def calcular_promedio(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]

    for nota in notas:
        if not isinstance(nota, (int, float)) or isinstance(nota, bool):
            raise ValueError("Las notas deben ser numeros.")

        if nota < 0 or nota > 100:
            raise ValueError("Las notas deben estar entre 0 y 100.")

    return sum(notas) / len(notas)


def determinar_estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"


def registrar_calificacion(nota1, nota2, nota3):
    promedio = calcular_promedio(nota1, nota2, nota3)

    return {
        "promedio": promedio,
        "estado": determinar_estado(promedio)
    }
