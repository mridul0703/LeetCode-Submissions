import os
import re

def generate_index(repo_path):
    # Get a list of files in the repository
    files = os.listdir(repo_path)

    # Filter out only the solution files based on the assumption they all start with numbers
    solution_files = [f for f in files if re.match(r'^\d+\.', f)]

    # Sort the files based on the leading number
    sorted_files = sorted(solution_files, key=lambda x: int(x.split('.')[0]))

    # Create an index file
    with open(os.path.join(repo_path, 'index.md'), 'w') as index_file:
        index_file.write("# LeetCode Solutions\n\n")
        for filename in sorted_files:
            index_file.write(f"- [{filename}](./{filename})\n")

    print("Index file has been generated successfully.")

if __name__ == "__main__":
    generate_index(os.getcwd())
