import sys
from pathlib import Path

# Agregar src al path de Python para que pytest encuentre los módulos
sys.path.insert(0, str(Path(__file__).parent / "src"))
