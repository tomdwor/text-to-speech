# Text to Speech Converter

A powerful Python command-line tool that converts text files into natural-sounding speech in multiple languages using Google's Text-to-Speech (gTTS) service. Perfect for creating audiobooks, learning materials, or accessibility solutions.

## Features

- 🌍 Support for 15 languages including English, Spanish, French, and more
- 📝 Processes plain text files (.txt) with UTF-8 encoding
- 🎧 Generates high-quality MP3 audio files
- 🚀 Simple command-line interface
- ⚡ Fast processing with error handling
- 📁 Automatic creation of output directories

## Requirements

- Python 3.12 or higher
- Internet connection (required for Google's Text-to-Speech service)
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tomdwor/text-to-speech.git
cd text-to-speech
```

2. Create and activate a virtual environment:
```bash
# On Unix/macOS
python3.12 -m venv .venv
source .venv/bin/activate

# On Windows
python3.12 -m venv .venv
.venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Command Structure
```bash
python text_to_speech.py -i <input_file> -o <output_file> -l <language_code>
```

### List Supported Languages
```bash
python text_to_speech.py --list-languages
```

### Examples

1. Convert English text to speech:
```bash
python text_to_speech.py -i data_examples/ibiza_en.txt -o output/ibiza_en.mp3 -l en
```

2. Convert Spanish text to speech:
```bash
python text_to_speech.py -i data_examples/ibiza_es.txt -o output/ibiza_es.mp3 -l es
```

### Command Line Arguments

| Argument | Short | Required | Description |
|----------|--------|----------|-------------|
| --input-file | -i | Yes* | Path to input text file (.txt) |
| --output-file | -o | Yes* | Path to output audio file (.mp3) |
| --language | -l | No | Language code (default: 'es') |
| --list-languages | - | No | Show available language codes |

\* Not required when using --list-languages

### Supported Languages

| Code | Language |
|------|----------|
| ar | Arabic |
| cs | Czech |
| de | German |
| en | English |
| es | Spanish |
| fr | French |
| hi | Hindi |
| it | Italian |
| ja | Japanese |
| ko | Korean |
| nl | Dutch |
| pl | Polish |
| pt | Portuguese |
| ru | Russian |
| zh | Chinese |

## Example Input Files

The repository includes example text files in the `data_examples` directory:

- `ibiza_en.txt` - English description of Ibiza
- `ibiza_es.txt` - Spanish description of Ibiza

## Output

- Audio files are saved in MP3 format
- Output directories are created automatically if they don't exist
- File paths can be relative or absolute

## Troubleshooting

### Common Issues

1. **FileNotFoundError**: 
   - Ensure the input file exists and the path is correct
   - Check if you're in the right directory

2. **Internet Connection Error**:
   - The tool requires an active internet connection to access Google's TTS service
   - Check your network connection if you get connection errors

3. **Invalid Language Code**:
   - Use `--list-languages` to see all supported language codes
   - Language codes are case-sensitive

### Best Practices

1. **Input Text**:
   - Use UTF-8 encoded text files
   - Keep paragraphs reasonably sized for better processing
   - Ensure proper punctuation for natural-sounding speech

2. **Output Files**:
   - Use .mp3 extension for output files
   - Ensure you have write permissions in the output directory

## Development

### Project Structure
```
text-to-speech/
├── data/
│   └── .gitignore
├── data_examples/
│   ├── ibiza_en.txt
│   └── ibiza_es.txt
├── data/
│   └── .output
├── .gitignore
├── README.md
├── requirements.txt
└── text_to_speech.py
```

### Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [gTTS](https://github.com/pndurette/gTTS) for providing the Text-to-Speech functionality
- Google Translate's Text-to-Speech engine

## Contact

For bug reports and feature requests, please use the [GitHub Issues](https://github.com/tomdwor/text-to-speech/issues) page.

## Blog article

[Building a Multilingual Text-to-Speech Tool with Python and gTTS - Tomasz Dworakowski Blog](https://www.tdworakowski.com/2024/11/building-multilingual-text-to-speech.html)
