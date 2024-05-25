import os
from collections import defaultdict

def count_labels(directory):
    labels_count = defaultdict(int)
    files = os.listdir(directory)
    for file in files:
        path = os.path.join(directory, file)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) >= 1:
                        label = int(parts[0])
                        labels_count[label] += 1
        except Exception as e:
            print(f"Error reading {path}: {e}")
    return labels_count

def main():
    train_labels_path = r'C:\Users\djdan\Desktop\IA\pythonProject\coco\labels\train'
    val_labels_path = r'C:\Users\djdan\Desktop\IA\pythonProject\coco\labels\val'

    print("Counting training labels...")
    train_labels_count = count_labels(train_labels_path)
    print("Counting validation labels...")
    val_labels_count = count_labels(val_labels_path)

    total_labels_count = defaultdict(int, train_labels_count)
    for label, count in val_labels_count.items():
        total_labels_count[label] += count

    print("Número de etiquetas únicas:", len(total_labels_count))
    print("Conteo de etiquetas:", dict(total_labels_count))

if __name__ == "__main__":
    main()

