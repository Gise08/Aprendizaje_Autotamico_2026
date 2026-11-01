# Clasificación de Resoluciones de Reclamos en el Servicio de Gas Natural (ENARGAS 2026)

Este repositorio contiene el desarrollo del proyecto de Aprendizaje Automático para la predicción temprana de resoluciones de reclamos de usuarios del servicio de distribución de gas natural en Argentina.

## Estructura del Repositorio

El proyecto sigue el estándar de organización de **Cookiecutter Data Science**:

```text
├── README.md                              <- Descripción general del proyecto
├── requirements.txt                       <- Dependencias y librerías necesarias
├── .gitignore                             <- Archivos y carpetas excluidos del control de versiones
├── data/
│   ├── raw/
│   │   └── reclamos_prestadoras_2026.csv  <- Dataset original público de ENARGAS (datos.gob.ar)
│   └── processed/
│       └── reclamos_procesados_2026.csv   <- Dataset desagregado y preprocesado (209.491 registros)
├── docs/
│   └── descripcion_dataset_y_origen.md    <- Documento técnico con diccionario y justificación metodológica
├── notebooks/
│   └── 01_exploracion_y_preprocesamiento.ipynb <- Notebook reproducible de carga, análisis y transformación
└── src/
    └── __init__.py