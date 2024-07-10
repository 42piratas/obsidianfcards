import os

# Function to read marked content from a file
def read_marked_content(file_path):
    marked_content = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            start = 0
            while True:
                start_index = line.find('{{fcards}}', start)
                end_index = line.find('{{/fcards}}', start_index)
                if start_index == -1 or end_index == -1:
                    break
                start_index += len('{{fcards}}')
                extracted_content = line[start_index:end_index].strip()
                marked_content.append(extracted_content)
                print(f'Extracted content from {file_path}: "{extracted_content}"')  # Debugging line
                start = end_index + len('{{/fcards}}')
    return marked_content

# Function to aggregate marked content from multiple files
def aggregate_marked_content(folder_path):
    all_marked_content = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):  # Assuming markdown files, change as needed
            file_path = os.path.join(folder_path, filename)
            marked_content = read_marked_content(file_path)
            all_marked_content.extend(marked_content)
            print(f'Aggregated content from {filename}: {marked_content}')  # Debugging line
    return all_marked_content

# Function to create a text file from the aggregated content
def create_text_file(content, output_path):
    with open(output_path, 'w') as file:
        for item in content:
            file.write(f'- {item}\n\n')

# Main function
def main():
    # Define the base path to your iCloud Obsidian documents
    base_path = 'Library/Mobile Documents/iCloud~md~obsidian/Documents'

    # Define the name of your vault and the selected folder within the vault
    vault_name = 'notes'  # Replace 'notes' with the name of your vault
    selected_folder = 'philosophy'  # Replace 'name' with the name of the specific folder within your vault

    # Combine the base path, vault name, and selected folder to form the full path
    notes_folder = os.path.expanduser(os.path.join('~', base_path, vault_name, selected_folder))

    # Aggregate content
    aggregated_content = aggregate_marked_content(notes_folder)

    # Debugging: Print the aggregated content
    print("Final Aggregated Content:")
    for content in aggregated_content:
        print(content)

    # Specify the output text file path
    output_text_path = os.path.expanduser('~/Downloads/fcards.txt')

    # Create the text file
    create_text_file(aggregated_content, output_text_path)

    print(f'Text file created successfully: {output_text_path}')

if __name__ == '__main__':
    main()
