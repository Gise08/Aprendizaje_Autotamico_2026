# Descripción del Dataset, Origen de los Datos y Marco Metodológico

## 1. Origen, Trazabilidad y Licenciamiento
* **Organismo emisor:** Ente Nacional Regulador del Gas (ENARGAS).
* **Portal de procedencia:** Portal Nacional de Datos Abiertos de la República Argentina (`datos.gob.ar`) / Catálogo de Datos Abiertos de ENARGAS.
* **Conjunto de datos:** Estadísticas de Reclamos de Usuarios del Servicio de Distribución de Gas por Redes.
* **Enlace de descarga:** `https://datos.gob.ar/dataset/enargas-reclamos-usuarios-servicio-distribucion-gas-por-redes`
* **Fecha de extracción:** Octubre de 2026.
* **Ventana temporal:** Enero a Agosto de 2026 (meses 1 a 8).
* **Condiciones de uso y régimen legal:** El conjunto se publica bajo la **Política de Datos Abiertos de la República Argentina** (Ley N° 27.275 de Acceso a la Información Pública y Decreto N° 117/2016). Constituye información pública gubernamental accesible sin restricciones comerciales para reutilización y fines de investigación, reconociendo la fuente oficial (no constituye transferencia patrimonial al dominio público en términos registrales).

---

## 2. Unidad de Análisis y Rol de la Variable `reclamo_cantidad`

### Naturaleza de los Datos Agregados
El conjunto contiene **3.454 registros agregados**. Cada fila resume mensualmente el volumen total de reclamos (`reclamo_cantidad`) que compartieron de manera sincrónica idéntica combinación de atributos (`reclamo_mes_nro`, `reclamo_prestadora`, `reclamo_provincia`, `reclamo_grupo`, `reclamo_via_ingreso`) y que obtuvieron la misma resolución administrativa (`reclamo_resolucion`).

El total consolidado es de **209.491 reclamos**.

### Clarificación Metodológica: Expansión vs. Prevención de Data Leakage
1. **Alcance de la expansión de filas:** La replicación de filas no crea observaciones genuinamente independientes ni añade variabilidad o atributos individuales a nivel usuario que el registro oficial no haya relevado; reproduce la función de probabilidad conjunta empírica de los reclamos. Para mantener trazabilidad rigurosa, cada registro conserva el `id_registro_agregado` que referencia a su fila original.
2. **Tratamiento del Data Leakage:** La prevención de la fuga de información radica estrictamente en **excluir `reclamo_cantidad` de la matriz de predictores ($X$)**. `reclamo_cantidad` es un agregado acumulado a mes vencido una vez cerrado el procesamiento administrativo; no está disponible al momento en que un usuario presenta un trámite.
3. **Temporalidad del registro:** La variable `reclamo_mes_nro` registra el mes de reporte consolidado administrativo ante la prestadora. Para evaluar la capacidad predictiva sobre eventos futuros, se adopta una partición estrictamente cronológica.

---

## 3. Diccionario de Variables

| Variable | Tipo de Dato | Rol | Definición y Justificación |
| :--- | :--- | :--- | :--- |
| `id_registro_agregado` | Entero (`int64`) | Identificador | Índice original de la tabla agregada para garantizar trazabilidad. |
| `reclamo_ano` | Entero (`int64`) | Informativo | Año 2026. Constante sin poder de discriminación (excluido de $X$). |
| `reclamo_mes_nro` | Entero (`int64`) | Predictor ($X$) / Eje Temporal | Mes (1 a 8). Se analiza tanto su rol de partición temporal como su tratamiento categórico para captar estacionalidad invernal. |
| `reclamo_mes_nombre` | Texto (`object`) | Descriptivo | Redundante con `reclamo_mes_nro` (excluido de $X$). |
| `reclamo_prestadora` | Categórico (`object`) | Predictor ($X$) | Distribuidora que recibió el trámite (9 licenciatarias). |
| `reclamo_provincia` | Categórico (`object`) | Predictor ($X$) | Jurisdicción donde radica el suministro (24 jurisdicciones). |
| `reclamo_grupo` | Categórico (`object`) | Predictor ($X$) | Tipo de motivo (Facturación, Suministro, Prestaciones). |
| `reclamo_via_ingreso` | Categórico (`object`) | Predictor ($X$) | Canal de recepción (Telefónico, Web, Presencial, etc.). |
| `reclamo_resolucion` | Binario (`int64`) | **Target ($y$)** | Resolución dictada: 1 = Procedente, 0 = Improcedente. |
| `reclamo_cantidad` | Entero (`int64`) | Ponderador | Frecuencia de casos. Excluida de $X$ por data leakage. |