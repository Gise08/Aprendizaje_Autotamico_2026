# Descripción del Dataset y Origen de los Datos

## 1. Origen y Fuente de los Datos
* **Organismo de procedencia:** Ente Nacional Regulador del Gas (ENARGAS), organismo autárquico regulador bajo la órbita de la Secretaría de Energía de la Nación.
* **Portal de publicación:** Portal Nacional de Datos Públicos (`datos.gob.ar` / Datos Abiertos ENARGAS).
* **Catálogo:** Estadísticas de Reclamos de Usuarios del Servicio de Distribución de Gas por Redes.
* **Período temporal:** Enero a Agosto de 2026 (meses 1 a 8).
* **Licencia:** Dominio público (Open Data), libre acceso y reutilización con fines académicos y de investigación.

---

## 2. Unidad de Análisis y Estructura del Dataset

### Distinción: Registros Agregados vs. Reclamos Unitarios
El conjunto de datos original consta de **3.454 filas** y **9 columnas**, sin presencia de valores nulos. 

Cada fila constituye un **resumen mensual agregado** que agrupa a los usuarios que compartieron idénticos atributos (mes, distribuidora, provincia, motivo y canal de atención) y obtuvieron la misma resolución. El volumen real total de reclamos auditados en el período asciende a **209.491 reclamos**, resultante de sumar la variable `reclamo_cantidad`.

### Balance de Clases y Tratamiento Metodológico de `reclamo_cantidad`
* **Distribución a nivel de filas agregadas:** 1.956 filas correspondientes a resoluciones *Improcedentes* (56,63%) frente a 1.498 filas *Procedentes* (43,37%).
* **Distribución a nivel de reclamos reales (ponderada por cantidad):** 148.647 reclamos *Improcedentes* (70,96%) frente a 60.844 reclamos *Procedentes* (29,04%).

**Exclusión de `reclamo_cantidad` como variable predictora:**
El objetivo del modelo consiste en estimar si un nuevo reclamo resultará *Procedente* o *Improcedente* al momento de su recepción. La variable `reclamo_cantidad` se construye a mes vencido, una vez concluida la evaluación administrativa. Utilizarla como variable de entrada ($X$) provocaría **fuga de datos (data leakage)**. Por ende, para el entrenamiento se adopta la desagregación de instancias (o ponderación por frecuencia), excluyendo `reclamo_cantidad` de los predictores.

---

## 3. Diccionario de Variables

| Variable | Tipo de Dato | Rol Metodológico | Descripción |
| :--- | :--- | :--- | :--- |
| `reclamo_ano` | Entero (`int64`) | Informativo | Año de registro (constante: 2026). Sin varianza para modelado. |
| `reclamo_mes_nro` | Entero (`int64`) | Predictor ($X$) | Número de mes de ingreso (1 a 8). |
| `reclamo_mes_nombre` | Texto (`object`) | Descriptivo | Nombre del mes (Enero a Agosto). Redundante con `reclamo_mes_nro`. |
| `reclamo_prestadora` | Texto (`object`) | Predictor ($X$) | Empresa prestadora receptora (9 empresas licenciatarias). |
| `reclamo_provincia` | Texto (`object`) | Predictor ($X$) | Jurisdicción provincial donde radica el suministro (24 provincias). |
| `reclamo_grupo` | Texto (`object`) | Predictor ($X$) | Tipología del reclamo (Facturación, Suministro, Prestaciones). |
| `reclamo_via_ingreso` | Texto (`object`) | Predictor ($X$) | Canal de recepción (Telefónico, Chat, Web, Personal, etc.). |
| `reclamo_resolucion` | Texto (`object`) | **Target ($y$)** | Dictamen final: `Procedente` o `Improcedente`. |
| `reclamo_cantidad` | Entero (`int64`) | Ponderador | Total de reclamos agrupados en dicha combinación estadística. |