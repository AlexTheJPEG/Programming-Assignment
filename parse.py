from PIL import Image, ImageDraw
import glob
import re

pattern = r"bounds=\"(\[(\d+),(\d+)\])(\[(\d+),(\d+)\])\""

for xml_file in glob.glob("Programming-Assignment-Data/*.xml"):
    name = xml_file[:-4]
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
            # Use regular expression to get rectangle coordinates of clickable boundary box
            matches = re.findall(pattern, line)[0]
            x1, y1, x2, y2 = int(matches[1]), int(matches[2]), int(matches[4]), int(matches[5])
            rects.append((x1, y1, x2, y2))
    print(rects)
    # Open image counterpart
    img_file = name + ".png"
    image = Image.open(img_file).convert("RGBA")
    draw = ImageDraw.Draw(image)
    # Highlight each clickable area and save as a new image
    for rect in rects:
        draw.rectangle(rect, outline="yellow", width=8)
    image.save(f"results/{name[28:]} new.png", "PNG")