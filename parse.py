from PIL import Image
import glob
import re

pattern = r"bounds=\"(\[(\d+),(\d+)\])(\[(\d+),(\d+)\])\""

for xml_file in glob.glob("Programming-Assignment-Data/*.xml"):
    print(xml_file)
    rects = []
    with open(xml_file, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        if len(lines) == 1:
            # Separate XML by lines if it's only 1 line
            lines = lines[0].split("><")
        for line in lines:
            # Go through each line and find a clickable node
            if "clickable=\"true\"" not in line:
                continue
            matches = re.findall(pattern, line)[0]
            x1, y1, x2, y2 = int(matches[1]), int(matches[2]), int(matches[4]), int(matches[5])
            rects.append((x1, y1, x2, y2))
    print(rects)
    print()