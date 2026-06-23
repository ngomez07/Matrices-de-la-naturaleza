# Matrices de la Naturaleza

Este repositorio contiene proyectos y recursos del portafolio de Nicolás Gómez, incluyendo archivos `.toe`, imágenes y un convertidor de video en Python.

## Contenido

- `convertir_mov.py`: script Python para convertir archivos `.mov` a `.mp4` usando FFmpeg.
- `Backup/`: versiones antiguas del proyecto.
- `convertidos/`: salida de conversión de video (no subida al repositorio).
- Archivos principales `.toe` y medios relacionados con el proyecto.

## Uso del convertidor de video

### Requisitos

- Python 3.x
- FFmpeg instalado y accesible desde el PATH.

### Ejecutar

```bash
python convertir_mov.py [ruta_del_directorio]
```

Si no se especifica directorio, el script buscará archivos `.mov` en el directorio actual.

### Qué hace

- busca archivos `.mov` recursivamente
- convierte cada archivo a `.mp4`
- usa `libx264`, `aac` y `-movflags +faststart`
- guarda los resultados en la carpeta `convertidos/`

## Notas

- No se incluyen archivos de video generados ni archivos grandes superiores a 100 MB en el repositorio.
- Si necesitas incluir archivos de medios grandes, considera usar Git LFS.
