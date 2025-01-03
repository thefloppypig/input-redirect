
import sys
import csv
from floppyconfig import controllerToInternalCodeMap

def main():
    if len(sys.argv) != 2:
        print("Usage: python converter.py <file-path>")
        return
    
    file_path = sys.argv[1]
    
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            input_stack = [row for row in reader if row[1] != "Sync"]
            print(f"Loaded {len(input_stack)} input events from file.")

            new_input_stack = []
            prev_time = 0
            for line in input_stack:
                curr_time = float(line[0])
                line[0] = str(curr_time - prev_time)
                if line[2] in controllerToInternalCodeMap:
                    line[2] = controllerToInternalCodeMap[line[2]]
                new_input_stack.append([line[0], line[2], line[3]])
                prev_time = curr_time

        new_file_path = file_path.split('.')[0] + '_converted.csv'
        with open(new_file_path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=' ')
            writer.writerows(new_input_stack)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()


