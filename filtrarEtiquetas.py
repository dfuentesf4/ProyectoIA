import os


def filter_labels(directory, max_label):
    files = os.listdir(directory)
    for file in files:
        path = os.path.join(directory, file)
        corrected_lines = []
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 1:
                    label = int(parts[0])
                    if label <= max_label:
                        corrected_lines.append(line)

        with open(path, 'w') as f:
            f.writelines(corrected_lines)


train_labels_path = r'C:\Users\djdan\Desktop\IA\pythonProject\coco\labels\train'
val_labels_path = r'C:\Users\djdan\Desktop\IA\pythonProject\coco\labels\val'

# Asegúrate de cambiar el valor de max_label a 79, que es el máximo para COCO con 80 clases
filter_labels(train_labels_path, 79)
filter_labels(val_labels_path, 79)
