import sys
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description="Example program that copies contents of one file to another.")
parser.add_argument("input", help="input filename")
parser.add_argument("output", help="output filename")
parser.add_argument("--option", action="store_true", help="script option")
parser.add_argument("--parameter", help="script parameter")
args = parser.parse_args()

input_filename = Path(args.input)
output_filename = Path(args.output)

if not input_filename.is_file():
    sys.stderr.write(f"Error: `{input_filename}` is not a valid file.")
    sys.exit(1)

with open(input_filename,"r") as file:
    input = file.read()

with open(output_filename, "w") as f:
    f.write(input)
    sys.stdout.write("Done!")