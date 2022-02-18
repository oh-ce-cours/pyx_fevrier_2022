from logging import root
from pathlib import Path
import tarfile
import puremagic
import argparse
import shutil


parser = argparse.ArgumentParser(description="Recover some files.")
parser.add_argument("path", type=str, help="the .tar(.gz) path to extract")
parser.add_argument(
    "--check",
    action="store_true",
    help="Should the actions be perfomed",
)

args = parser.parse_args()
tar_file = args.path
check = args.check
print(tar_file)
print(check)


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
    new_file_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, new_file_path)
shutil.make_archive("recovered", format="zip", root_dir=recovered)
shutil.rmtree(recovered)
shutil.rmtree(extracted)
