import argparse
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser(
    prog='JPGtoPNGConverter',
    description='Convert all files in source directory from JPG to PNG and save them to destination directory.')

parser.add_argument('-sf', '--source_folder', type=str, required=True)
parser.add_argument('-df', '--destination_folder', type=str, required=True)
args = parser.parse_args()

if(not Path(args.source_folder).exists()):
    print('Source folder does not exist')

if(not Path(args.destination_folder).exists()):
    print('Destination folder does not exist. Creating...')
    try:
        Path(args.destination_folder).mkdir()
        print(f'Destination folder {args.destination_folder} created.')
    except IOError as err:
        print(err)
        
for file in Path(args.source_folder).iterdir():
    img = Image.open(file)
    new_path = Path(args.destination_folder)
    img.save(f"{new_path.joinpath(file.stem)}.png", "png")
