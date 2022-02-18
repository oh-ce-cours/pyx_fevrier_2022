from logging import root
from pathlib import Path
import tarfile
import puremagic
import click
import shutil


def untar(tar_filename, extract_path):
    if tar_filename.endswith("tar.gz"):
        tar = tarfile.open(tar_filename, "r:gz")
        tar.extractall(extract_path)
        tar.close()
    elif tar_filename.endswith("tar"):
        tar = tarfile.open(tar_filename, "r:")
        tar.extractall(extract_path)
        tar.close()


extracted = Path(".") / "extracted"
recovered = Path(".") / "recovered"


@click.command()
@click.argument("tar_file", default="")
@click.option("--check", prompt="Your name", help="The person to greet.")
def main(tar_file, check):
    untar(tar_file, extracted)
    for path in extracted.iterdir():
        correct_extention = puremagic.from_file(str(path))
        if "jfif" in correct_extention:
            correct_extention = ".jpg"

        extension_without_point = correct_extention[1:]
        new_name = path.parts[-1].split(".")[0]
        new_name = f"{new_name}.{extension_without_point}"
        new_file_path = recovered / extension_without_point / new_name
        print(f"{path} => {new_file_path}")
        if not check:
            new_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, new_file_path)
        else:
            print(f"should create {new_file_path.parent}")

    if not check:
        shutil.make_archive("recovered", format="zip", root_dir=recovered)
        shutil.rmtree(recovered)
        shutil.rmtree(extracted)
    else:
        print("should create archive")


if __name__ == "__main__":
    main()
