
# Experimento Escalabilidad - Prodcuts API

Repositorio que contiene el experimento de Escalabilidad del Grupo 7

# Experimento ASR13 - Escalabilidad a 400 Usuarios Concurrentes

Este proyecto implementa un experimento de arquitectura para validar el requisito de seguridad ASR-13 en MediSupply:

*Validar que las decisiones de escalabilidad se mantengan en un aumento del número de usuarios de manera concurrente en una campaña sanitaria, manteniendo transacciones sin perdida al alcanzar 400 usuarios concurrentes, cumpliendo el ASR-13 en ambiente de operación de aumento de demanda.*

El entorno se ejecuta en contenedores Docker e incluye:

* API Gateway - NGINX: Centraliza las entradas de cada una de las peticiones de los usuarios y utiliza balanceo round robin.
* 4 Replicas: (Products-API) Se disponen en el sistema 4 replicas del products api para insertar productos en el sistema. Dichas replicas hacen balanceo mediante round robin para satisfacer las transacciones de los 400 usuarios. Cada replica tiene un pool de 50 conexiones.
* Persistencia en Postgresql: 200 Conexiones dispuesta en el motor de base de datos. 

# Como Correr el Experimento

1. Clonar el repositorio o descargar el zip:
   
   ```git clone https://github.com/wpiarpuzan/escalabilidad-products-api.git```
3. Ir a la carpeta raíz del proyecto:
   
   ```cd escalabilidad-products-api```
4. Levantar los contenedores:

   ```docker-compose up --build```
5. Revise el estado de salud de la aplicación

   ```curl -X GET http://localhost/health -H "Content-Type: application/json" -sS```

## Ejecutar las Pruebas - Locust

## Analizar Resultados P95 / P99
1. Ir a la carpeta raíz del proyecto:

   ```cd escalabilidad-products-api```
2. Ingrese a la carpeta de metricas

   ```cd metrics```
3. Ejecute el archivo de metricas

   ```python analyze_metrics.py```

Retornará un resultado como:

   P95: 0.0214s
   P99: 0.0557s
   Success Rate: 100.00%

# Autores
Karen Tarazona - Felipe Rivera - Andrés Piarpuzan - Juan Pablo Camacho
