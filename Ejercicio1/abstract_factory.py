from abc import ABC, abstractmethod

# Interfaz Abstract Factory
class DataFactory(ABC):
    @abstractmethod
    def create_statistical_analysis(self):
        pass
    
    @abstractmethod
    def create_data_visualization(self):
        pass

class StatisticalAnalysisFactory(DataFactory):
    def create_statistical_analysis(self):
        return MeanAnalysis()  # Puedes cambiar esto a otras clases concretas según necesites
    
    def create_data_visualization(self):
        return None

# Clase concreta de fábrica para visualizaciones gráficas
class DataVisualizationFactory(DataFactory):
    def create_statistical_analysis(self):
        return None
    
    def create_data_visualization(self):
        return HistogramVisualization()  # Puedes cambiar esto a otras clases concretas según necesites

# Interfaz Abstract Product para análisis estadísticos
class StatisticalAnalysis(ABC):
    @abstractmethod
    def perform_analysis(self, data):
        pass

# Clase concreta de producto para análisis estadísticos
class MeanAnalysis(StatisticalAnalysis):
    def perform_analysis(self, data):
        return sum(data) / len(data)

class ModeAnalysis(StatisticalAnalysis):
    def perform_analysis(self, data):
        from statistics import mode
        return mode(data)

class MedianAnalysis(StatisticalAnalysis):
    def perform_analysis(self, data):
        from statistics import median
        return median(data)

# Interfaz Abstract Product para visualizaciones de datos
class DataVisualization(ABC):
    @abstractmethod
    def create_chart(self, data):
        pass

# Clase concreta de producto para visualizaciones de datos
class HistogramVisualization(DataVisualization):
    def create_chart(self, data):
        import matplotlib.pyplot as plt
        plt.hist(data, bins=10, color='blue', edgecolor='black')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.title('Histograma')
        plt.show()

def generate_report(factory, data):
    # Crear instancias de los análisis estadísticos
    mean_analysis = MeanAnalysis()
    mode_analysis = ModeAnalysis()
    median_analysis = MedianAnalysis()

    # Realizar análisis estadísticos
    result_mean = mean_analysis.perform_analysis(data)
    result_mode = mode_analysis.perform_analysis(data)
    result_median = median_analysis.perform_analysis(data)

    # Imprimir resultados
    print("Resultado del análisis de media:", result_mean)
    print("Resultado del análisis de moda:", result_mode)
    print("Resultado del análisis de mediana:", result_median)

    data_visualization = factory.create_data_visualization()

    if data_visualization:
        data_visualization.create_chart(data)




if __name__ == "__main__":
    import pandas as pd
    datos = pd.read_csv('Ejercicio1/dataset_limpio.csv', delimiter = ",")
    hora = datos["Hora Intervención"]

    

    factory = StatisticalAnalysisFactory()
    generate_report(factory, hora)

    visualization_factory = DataVisualizationFactory()
    generate_report(visualization_factory, hora)
