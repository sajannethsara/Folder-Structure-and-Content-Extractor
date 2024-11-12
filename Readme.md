# Extractor

**Extractor** is a command-line tool that simplifies working with large codebases when seeking AI assistance (e.g., ChatGPT). Instead of manually copying and pasting files one by one, Extractor automatically generates a single, organized file containing your project’s file structure and content. This makes it easy to provide a full view of your codebase to AI tools, allowing for smoother, more efficient coding and debugging assistance.

## Features

- **Easy File Structure Extraction**: Extracts the file structure of your project directory.
- **Content Compilation**: Compiles the content of all text files in the specified directory and subdirectories into one output file.
- **Ideal for AI Assistance**: Provides a single, comprehensive file for AI (e.g., ChatGPT) to understand your codebase, eliminating the need for tedious copy-pasting.

## Requirements

- **Python 3.x**: Make sure you have Python 3 installed on your system.

## Installation

Clone this repository and navigate to the directory :
```bash
git clone https://github.com/yourusername/Extractor.git
cd Extractor
```

Usage :
```bash
python Extractor.py "File Path That you want to extract file structure and the content into one file"
```
Example :
```bash
python Extractor.py "C:\path\to\your\project_folder"
```