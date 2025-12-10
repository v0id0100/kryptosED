# KryptosED

![Icono de la App](utils/images/icon.png)

## Español

## Visión General

**KryptosED** es una herramienta fácil de usar para cifrar y descifrar archivos y carpetas, diseñada con una interfaz moderna usando `customtkinter`. Esta aplicación proporciona cifrado AES-256 robusto con una barra de progreso en tiempo real, permitiéndote monitorear las operaciones de cifrado/descifrado. Ya sea que quieras proteger tus datos sensibles, experimentar con criptografía o personalizar tu espacio de trabajo, esta aplicación combina seguridad con características amigables para el usuario.

---

## ¿Por qué Usar Esta Aplicación?

- **Seguridad de Grado Militar:** Utiliza cifrado AES-256, el mismo estándar confiado por gobiernos y expertos en seguridad en todo el mundo.
- **Seguimiento de Progreso en Tiempo Real:** Monitorea las operaciones de cifrado/descifro con una barra de progreso visual que se actualiza a medida que se procesan los archivos.
- **Protege Tus Datos:** Cifra fácilmente información sensible para mantenerla privada de accesos no autorizados.
- **Aprende sobre Cifrado:** Perfecta para estudiantes y entusiastas para entender conceptos de cifrado moderno.
- **Personaliza Todo:** Cambia fuentes, colores e imágenes para hacer la aplicación verdaderamente tuya.
- **Vista Previa de Fuentes:** Ve instantáneamente cómo se ven diferentes fuentes antes de aplicarlas.

---

## Características

- **Cifrado/Descifrado de Archivos AES-256:**  
  Cifra o descifra archivos con modo AES-256-CTR, uno de los estándares de cifrado más seguros disponibles. Cada cifrado genera una clave criptográfica única para máxima seguridad.

- **Visualización de Progreso en Tiempo Real:**  
  Observa el progreso del cifrado/descifro con una barra de progreso dinámica que se actualiza a medida que se procesa cada bloque de 64KB.

- **Gestión Segura de Claves:**  
  Las claves de cifrado se generan de forma segura y se guardan como archivos binarios. Opción para eliminar automáticamente las claves después de un descifro exitoso.

- **Interfaz Moderna y Personalizable:**  
  Construida con `customtkinter` para una interfaz elegante y moderna con fácil personalización de apariencia.

- **Utilidad de Vista Previa de Fuentes:**  
  Usa `test_fonts.py` para previsualizar y seleccionar entre una amplia gama de fuentes antes de implementarlas en la aplicación principal.

- **Soporte para Imágenes e Iconos:**  
  Cambia fácilmente imágenes e iconos para personalizar tu experiencia.

- **Soporte para Múltiples Archivos vía Compresión:**  
  Cifra múltiples archivos comprimiéndolos primero en un solo archivo, luego cifrando el archivo como un único archivo seguro.

---

## Comenzando

### 1. Instalación

Asegúrate de tener Python 3.7+ instalado. Luego, instala las librerías requeridas:

```bash
pip install -r requirements.txt
```

**Librerías Requeridas:**
- `PyCryptodome` - Para implementación de cifrado AES-256
- `customtkinter` - Para componentes de interfaz moderna
- `tkinter` - Para elementos GUI y barras de progreso
- `Pillow` - Para manipulación y soporte de imágenes

### 2. Ejecutando la Aplicación

Ejecuta el paquete Python:

```bash
python -m KryptosED
```

### 3. Cifrando Archivos

1. Haz clic en "Cifrar Archivo" en la interfaz principal
2. Selecciona el archivo que quieres cifrar
3. Aparecerá una barra de progreso mostrando el progreso del cifrado en tiempo real
4. Después de completar el cifrado, elige una ubicación para guardar tu clave de cifrado
5. El archivo cifrado ahora reemplaza al original (¡guarda el archivo de clave de forma segura para el descifro!)

### 4. Descifrando Archivos

1. Haz clic en "Descifrar Archivo" en la interfaz principal
2. Selecciona el archivo cifrado
3. Selecciona el archivo `.key.bin` correspondiente
4. Observa la barra de progreso mientras tu archivo se descifra
5. Elige si quieres mantener o eliminar el archivo de clave después del descifro

### 5. Múltiples Archivos (Compresión)

Para cifrar o descifrar varios archivos a la vez, usa la función de compresión de la aplicación:
1. Selecciona múltiples archivos o una carpeta que contenga tus archivos.
2. La aplicación los comprimirá automáticamente en un solo archivo (ej. ZIP).
3. El archivo comprimido se cifra o descifra como un único archivo con seguimiento de progreso.
4. Después del descifro, el archivo comprimido puede extraerse para restaurar los archivos originales.

*Esto es útil para manejar de forma segura lotes de archivos y mantener todo organizado.*

---

## Detalles Técnicos

### Método de Cifrado
- **Algoritmo:** AES-256 (Estándar de Cifrado Avanzado con clave de 256 bits)
- **Modo:** CTR (Modo Contador) - Proporciona seguridad semántica y procesamiento paralelo
- **Generación de Clave:** Generación de clave aleatoria criptográficamente segura (32 bytes)
- **Nonce:** Nonce aleatorio de 8 bytes para modo CTR, almacenado con el archivo cifrado

### Características de Seguridad
- Cada operación de cifrado genera una clave única y aleatoria
- Las claves nunca se almacenan con los datos cifrados
- Sin reutilización de contraseñas - cada archivo obtiene su propia clave criptográfica
- La barra de progreso no compromete la seguridad - solo muestra el estado del procesamiento

### Rendimiento
- Procesa archivos en bloques de 64KB para eficiencia de memoria
- Actualizaciones de progreso en tiempo real durante el procesamiento
- Soporta archivos de cualquier tamaño
- Sobrecarga mínima de rendimiento para cifrado fuerte

---

## Personalizando la Aplicación

### Fuentes

- Abre `src/operation/utils/test_fonts.py` y ejecútalo:
  ```bash
  python src/operation/utils/test_fonts.py
  ```
- Navega por las muestras de fuentes.  
- Aplica tu fuente elegida en la aplicación principal actualizando la sección de código relevante (ver comentarios en el código).

### Imágenes

- Añade tus archivos de imagen a /images y cambia su nombre a `icon.png`.
- Actualiza las rutas de las imágenes en el código en la variable `title_letter` y `font_letter` en `main.py`.
- Reinicia la aplicación para ver tus cambios.

### Colores y Estilos

- Modifica los parámetros de color y estilo en el código (busca configuraciones de `customtkinter`).
- Experimenta con diferentes temas y diseños.

### Personalización de la Barra de Progreso
La barra de progreso puede personalizarse en `encryption.py` y `decryption.py`:
- Cambia el tamaño del bloque para diferentes características de rendimiento
- Modifica la apariencia de la barra de progreso (color, longitud, estilo)
- Añade etiquetas de porcentaje o estimaciones de tiempo

---

## Compilando a un Ejecutable (.exe)

¿Quieres compartir tu aplicación como un ejecutable independiente para Windows?

1. Instala PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Compila tu aplicación:
   ```bash
   pyinstaller --onefile --windowed --name KryptosED --icon=KryptosED/utils/images/icon.png --add-data "KryptosED/utils/images/icon.png;KryptosED/utils/images" KryptosED/__main__.py
   ```
3. Encuentra tu `.exe` en la carpeta `dist`.

**Nota:**  
PyInstaller empaqueta automáticamente todas las dependencias requeridas de tu entorno Python en el ejecutable. No necesitas instalar dependencias por separado en la máquina destino.

---

## Mejores Prácticas de Seguridad

1. **Siempre haz copia de seguridad de tus claves de cifrado** - Sin la clave, los archivos cifrados son irrecuperables
2. **Almacena las claves separadas de los datos cifrados** - Nunca las mantengas en la misma ubicación
3. **Usa contraseñas fuertes** para tu sistema donde se almacenan las claves
4. **Elimina las claves de forma segura** después de usarlas si ya no necesitas acceso a los datos
5. **Verifica la integridad del archivo** después del descifro comprobando tamaños y extensiones de archivo

---

## Solución de Problemas

- **"ModuleNotFoundError: No module named 'Crypto'"**  
  Instala PyCryptodome: `pip install pycryptodome`

- **La barra de progreso no se actualiza**  
  Asegúrate de estar ejecutando la versión más reciente con los módulos de cifrado/descifro actualizados

- **El descifro falla**  
  Verifica que estés usando el archivo de clave correcto para el archivo cifrado. Cada clave es única para su archivo.

- **Los archivos grandes tardan tiempo**  
  Esto es normal - AES-256 está procesando cada byte de tu archivo para máxima seguridad

---

## Créditos

- Desarrollado por **v0id0100**
- Usa la librería **PyCryptodome** para implementación AES-256
- Construido con **customtkinter** para componentes GUI modernos
- Implementación de barra de progreso usando **tkinter.ttk**

---

## Historial de Versiones

### v1.1.0
- Añadidas barras de progreso en tiempo real para cifrado/descifro
- Implementación mejorada de AES-256-CTR
- Interfaz de gestión de claves mejorada
- Mejor manejo de errores y retroalimentación al usuario

### v1.0.0
- Lanzamiento inicial con cifrado/descifro básico
- Interfaz personalizable con vista previa de fuentes
- Soporte de compresión de archivos para operaciones por lotes

---

**Descargo de responsabilidad:** Esta herramienta es para uso educativo y personal. Los desarrolladores no son responsables de ninguna pérdida de datos o brechas de seguridad resultantes del uso incorrecto de este software. Siempre mantén copias de seguridad de datos importantes antes de operaciones de cifrado.