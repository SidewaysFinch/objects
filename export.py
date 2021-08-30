from pathlib import Path
import os
from importlib import import_module

from cadquery import exporters

export_types = [
    ".stl",
    ".step",
    ".amf",
]


def main():
    for root, _, files in os.walk("."):
        for f in files:
            path = Path(root) / f
            if path.suffix == ".py" and path.stem != "export":
                module = ".".join(path.with_suffix("").parts)
                print(f"Importing {module}")
                mod = import_module(module)
                result = mod.result

                for t in export_types:
                    export_path = path.with_suffix(t)
                    print(f"Exporting to {export_path}")
                    exporters.export(result, str(export_path))

if __name__ == "__main__":
    main()