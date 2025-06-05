import re
import meshio
import numpy as np


def read_geo(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    variables = {}
    points = {}
    lines_data = []
    fixed_nodes = []
    load_nodes = []

    # Pass 1: Collect variables
    for line in lines:
        var_match = re.match(r"^\s*(\w+)\s*=\s*([\d\.]+);", line)
        if var_match:
            var_name, value = var_match.groups()
            variables[var_name] = float(value)

    # Pass 2: Read points
    for line in lines:
        match = re.match(r"Point\((\d+)\)\s*=\s*{\s*(.*?)\s*};", line)
        if match:
            idx = int(match.group(1))
            raw_coords = match.group(2).split(",")[:3]
            coords = []
            for val in raw_coords:
                val = val.strip()
                try:
                    coords.append(float(val))
                except ValueError:
                    # Simple variable substitution like "2*L"
                    for var in variables:
                        val = val.replace(var, str(variables[var]))
                    coords.append(eval(val))  # use with care
            points[idx] = coords

    # Pass 3: Read lines (connectivity)
    for line in lines:
        match = re.match(r"Line\((\d+)\)\s*=\s*{\s*(\d+),\s*(\d+)\s*};", line)
        if match:
            start, end = int(match.group(2)), int(match.group(3))
            lines_data.append([start-1, end-1])  # 0-based

    # Pass 4: Physical groups
    for line in lines:
        if "Physical Point" in line:
            if "FixedNodes" in line:
                fixed_nodes = [int(x)-1 for x in re.findall(r"\d+", line)]
            elif "LoadNodes" in line:
                load_nodes = [int(x)-1 for x in re.findall(r"\d+", line)]

    coords_array = [points[i+1] for i in range(len(points))]
    return {
        "nodal_coordinates": coords_array,
        "connectivity": lines_data,
        "fixed_nodes": fixed_nodes,
        "load_nodes": load_nodes
    }


if __name__ == "__main__":
    filepath = "meshes//frame3d.geo"

    data = read_geo(filepath)

    print("Nodal coordinates:\n", np.array(data["nodal_coordinates"]))
    print("Connectivity:\n", np.array(data["connectivity"]))
    print("Fixed Nodes:", data.get("fixed_nodes", []))
    print("Load Nodes:", data.get("load_nodes", []))


