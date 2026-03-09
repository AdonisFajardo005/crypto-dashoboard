# Crypto Market Dashboard

Dashboard interactivo para analizar precios de criptomonedas en tiempo real utilizando Python.

## Descripción

Este proyecto es una aplicación web que permite visualizar y analizar datos de criptomonedas utilizando datos obtenidos desde una API pública.
El sistema permite seleccionar diferentes criptomonedas, visualizar su evolución de precio y analizar métricas del mercado.

El objetivo del proyecto es demostrar habilidades en:

* consumo de APIs
* análisis de datos
* visualización interactiva
* desarrollo de dashboards en Python

## Tecnologías utilizadas

* Python
* Pandas
* Requests
* Plotly
* Streamlit

## Funcionalidades

El dashboard permite:

* seleccionar diferentes criptomonedas
* visualizar el precio histórico
* calcular promedio móvil
* mostrar estadísticas del mercado
* visualizar retornos del mercado
* explorar los datos en una tabla interactiva

## Fuente de datos

Los datos utilizados en el proyecto provienen de la API pública de CoinGecko.

## Instalación

Clonar el repositorio:

```git clone https://github.com/AdonisFajardo005/crypto-dashoboard.git```

Entrar a la carpeta del proyecto:

```cd crypto-dashboard```

Crear entorno virtual:

```python -m venv venv```

Activar entorno virtual:

Windows

```venv\Scripts\activate```

Instalar dependencias:

```pip install -r requirements.txt```

## Ejecución del proyecto

Para ejecutar el dashboard:

```streamlit run app.py```

La aplicación se abrirá automáticamente en el navegador.

## Estructura del proyecto

crypto-dashboard
│
├── app.py
├── crypto_api.py
├── analysis.py
├── requirements.txt
└── README.md

## Autor

Adonis Fajardo
