"""Build both resumes from any working directory: python resume/build.py."""
from importlib.metadata import version
from pathlib import Path
import argparse
import typst

ROOT = Path(__file__).resolve().parent
OUTPUTS = {"ru": "CV_Хрестьяновский_Даниил.pdf", "en": "CV_Khrestianovskii_Daniil.pdf"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lang", choices=["ru", "en", "all"], default="all")
    parser.add_argument("--output-dir", type=Path, default=ROOT)
    args = parser.parse_args()
    if version("typst") != "0.15.0":
        parser.error("Install the pinned compiler: python -m pip install -r resume/requirements.txt")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    languages = OUTPUTS if args.lang == "all" else [args.lang]
    # Compile everything before replacing any deliverable.
    documents = {lang: typst.compile(
        str(ROOT / "resume.typ"), root=str(ROOT),
        font_paths=[str(ROOT / "fonts")], ignore_system_fonts=True,
        sys_inputs={"lang": lang}, timestamp=0,
    ) for lang in languages}
    for lang, pdf in documents.items():
        target = args.output_dir / OUTPUTS[lang]
        target.write_bytes(pdf)
        print(target)


if __name__ == "__main__":
    main()
