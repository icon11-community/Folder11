import os
from typing import Tuple, List, Dict
import subprocess
from pathlib import Path

def convert_svg_to_ico(input_folder:str, output_folder:str, sizes:Tuple[int, ...]=(16,32,48,64,256)):
    """
    Converts a folder of .svg icons to a folder of .ico icons of various sizes.
    Icons can be swapped based on a maximum size attributed to .svg icons, if their name ends with '-{size}px.svg'.
    This function requires Imagemagick to be installed.

    Args:
        input_folder (str): The path to the folder containing the .svg icons.
        output_folder (str): The path to the folder where the .ico icons will be saved.
        sizes (Tuple[int, ...], optional): The sizes of the .ico icons. Defaults to (16, 32, 48, 64, 256).
    """
    
    def ends_with_px(string:str) -> bool:
        if not string.endswith('px'): return False
        parts:Tuple[str, ...] = string.rsplit('-', 1)
        if len(parts) != 2: return False
        return parts[1][:-2].isdigit()
    
    def delete_folder(folder_path):
        folder = Path(folder_path)
        if folder.exists() and folder.is_dir():
            for item in folder.iterdir():
                if item.is_file():
                    item.unlink()
        folder.rmdir()
    
    sizes = sorted(sizes)

    base_filenames:List[str] = [filename for filename in os.listdir(input_folder) if filename.lower().endswith('.svg') 
        and not any([ends_with_px(filename[:-4].lower()) for s in sizes])]
    alt_filenames:List[str] = [filename for filename in os.listdir(input_folder) if filename.lower().endswith('.svg') 
        and any([ends_with_px(filename[:-4].lower()) for s in sizes[:-1]])]
    
    # Iterate through all base .svg files in the input folder
    for base_filename in base_filenames:
        # print(base_filename)
        inputs:List[Dict[str, int | str]] = []

        for size in sizes:
            assumed_filename:str = base_filename[:-4] + f'-{size}px.svg'
            if assumed_filename not in alt_filenames: continue
            
            alt_input_path:str = os.path.join(input_folder, assumed_filename)
            
            inputs.append({'path': alt_input_path, 'maximum_size': size})
        
        # Add version that comes for sizes above alt max sizes
        inputs.append({'path': os.path.join(input_folder, base_filename), 'maximum_size': sizes[-1]})
        
        # Step 1: Convert input.svg's to throughput.png's using Imagemagick
        Path("temp_pngs").mkdir(parents=True, exist_ok=True)
        throughput_paths:List[str] = [os.path.join("temp_pngs", f'{base_filename[:-4]}-{size_index}.png') for size_index in range(len(sizes))]
        size_index:int = 0
        # print(inputs)
        input:Dict[str, int | str] = inputs.pop(0)
        for size_index in range(len(sizes)):
            # Go to next input if the current needed size is greater than input's maximum
            if sizes[size_index] > input['maximum_size']:
                input:Dict[str, int | str] = inputs.pop(0)
            # print(input)
            current_size:int = sizes[size_index]
            throughput_path:str = throughput_paths[size_index]
            try:
                # magick convert -background transparent <input> -resize <maximum_size>x<maximum_size> <output>
                subprocess.run([
                    'magick',
                    'convert',
                    '-background', 'transparent',
                    input['path'],
                    '-resize', f'{current_size}x{current_size}',
                    throughput_path
                ], check=True)
                # print(f"Converted {base_filename} to {throughput_path}")
            except subprocess.CalledProcessError as e:
                print(f"SVG2PNG: Error converting {base_filename}: {e}")
            size_index += 1
        
        # Step 2: Combine throughput.png's to final output.ico using Imagemagick
        Path(output_folder).mkdir(parents=True, exist_ok=True)
        output_filename:str = os.path.splitext(base_filename)[0] + '.ico'
        output_path:str = os.path.join(output_folder, output_filename)
        try:
            # magick convert input-1.png input-2.png ... input-n.png output.ico
            subprocess.run([
                'magick',
                'convert',
                '-background', 'transparent',]
                + throughput_paths
                + [output_path], 
                check=True)
            print(f"Converted {base_filename} to {output_filename}")
        except subprocess.CalledProcessError as e:
            print(f"PNG2ICO: Error converting {base_filename}: {e}")
        
    delete_folder("temp_pngs")

if __name__ == "__main__":
    # Input folder containing .svg files
    input_folder:str = input("Input folder (leave blank for default): ")
    # Output folder for converted .ico files 
    output_folder:str = input("Output folder (leave blank for default): ")
    # List of icon sizes
    sizes:List[int] = [s for s in map(int, input("Icon sizes (leave blank for default): ").split()) if s > 0]
    
    input_folder = "svg/" if not input_folder else input_folder
    output_folder = "ico/" if not output_folder else output_folder
    sizes = [16, 32, 48, 64, 256] if not sizes else sizes
    
    convert_svg_to_ico(input_folder, output_folder)