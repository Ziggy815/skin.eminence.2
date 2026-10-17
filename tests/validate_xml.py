import os
import xml.etree.ElementTree as ET
import sys

def validate_xml_files(root_dir):
    """
    Recursively finds and validates all XML files in the root_dir.
    Skips the .git directory.
    """
    invalid_files = []
    for root, dirs, files in os.walk(root_dir):
        # Skip .git directory
        if '.git' in dirs:
            dirs.remove('.git')

        for file in files:
            if file.endswith('.xml'):
                file_path = os.path.join(root, file)
                try:
                    ET.parse(file_path)
                except ET.ParseError as e:
                    invalid_files.append((file_path, str(e)))

    return invalid_files

if __name__ == "__main__":
    # Assuming the script is in the 'tests' directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Validating XML files in: {base_dir}")
    errors = validate_xml_files(base_dir)

    if errors:
        print(f"Found {len(errors)} invalid XML file(s):")
        for file_path, error in errors:
            # Print path relative to base_dir for cleaner output
            rel_path = os.path.relpath(file_path, base_dir)
            print(f"  {rel_path}: {error}")
        sys.exit(1)
    else:
        print("All XML files are valid.")
        sys.exit(0)
