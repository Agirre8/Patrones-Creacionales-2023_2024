from abstract_factory import *
if __name__ == "__main__":
    import pandas as pd
    datos = pd.read_csv('Ejercicio1/dataset_limpio.csv', delimiter = ",")
    hora = datos["Hora Intervención"]

    

    factory = StatisticalAnalysisFactory()
    generate_report(factory, hora)

    visualization_factory = DataVisualizationFactory()
    generate_report(visualization_factory, hora)