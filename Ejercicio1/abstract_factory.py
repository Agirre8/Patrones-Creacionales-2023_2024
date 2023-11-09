from abc import ABC, abstractmethod

# Interfaz Abstract Factory
class DataFactory(ABC):
    @abstractmethod
    def create_statistical_analysis(self):
        pass
    
    @abstractmethod
    def create_data_visualization(self):
        pass

# Clase concreta de fábrica para análisis estadísticos
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
# Ejemplo de uso
def generate_report(factory, data):
    statistical_analysis = factory.create_statistical_analysis()
    data_visualization = factory.create_data_visualization()
    
    if statistical_analysis:
        result = statistical_analysis.perform_analysis(data)
        print("Resultado del análisis estadístico:", result)
    
    if data_visualization:
        data_visualization.create_chart(data)

if __name__ == "__main__":
    import pandas as pd
    datos = pd.read_csv('Ejercicio1/dataset_limpio.csv', delimiter = ",")
    hora = datos["Hora Intervención"]

    statistical_factory = StatisticalAnalysisFactory()
    generate_report(statistical_factory, hora)
    
    visualization_factory = DataVisualizationFactory()
    generate_report(visualization_factory, hora)
