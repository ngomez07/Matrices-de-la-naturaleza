import os
import subprocess
import sys
from pathlib import Path


def find_ffmpeg():
    """Busca ffmpeg en el sistema."""
    result = subprocess.run(
        ["where", "ffmpeg"], capture_output=True, text=True, shell=True
    )
    if result.returncode == 0:
        return "ffmpeg"

    common_paths = [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
    ]
    for path in common_paths:
        if os.path.exists(path):
            return path

    return None


def convert_mov_to_mp4(search_dir="."):
    search_path = Path(search_dir).resolve()
    output_dir = search_path / "convertidos"
    output_dir.mkdir(exist_ok=True)

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        print("ERROR: ffmpeg no encontrado.")
        print("Instálalo desde https://ffmpeg.org/download.html")
        print("O instala con: winget install Gyan.FFmpeg")
        sys.exit(1)

    mov_files = list({
        f.resolve()
        for f in search_path.rglob("*")
        if f.suffix.lower() == ".mov"
    })

    if not mov_files:
        print(f"No se encontraron archivos .mov en: {search_path}")
        return

    print(f"Encontrados {len(mov_files)} archivo(s) .mov\n")

    for i, mov_file in enumerate(mov_files, 1):
        output_name = mov_file.stem + ".mp4"
        output_path = output_dir / output_name

        print(f"[{i}/{len(mov_files)}] Convirtiendo: {mov_file.name}")
        print(f"           -> {output_path}")

        cmd = [
            ffmpeg,
            "-i", str(mov_file),
            "-vcodec", "libx264",
            "-profile:v", "high",
            "-level:v", "4.2",
            "-pix_fmt", "yuv420p",  # necesario para compatibilidad con Windows
            "-crf", "18",
            "-preset", "medium",
            "-acodec", "aac",
            "-b:a", "192k",
            "-movflags", "+faststart",
            "-y",
            str(output_path),
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            original_mb = mov_file.stat().st_size / (1024 * 1024)
            output_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"           OK  {original_mb:.1f} MB -> {output_mb:.1f} MB\n")
        else:
            print(f"           ERROR al convertir {mov_file.name}")
            print(result.stderr[-500:])
            print()

    print(f"Listo. Archivos guardados en: {output_dir}")


if __name__ == "__main__":
    directorio = sys.argv[1] if len(sys.argv) > 1 else "."
    convert_mov_to_mp4(directorio)
