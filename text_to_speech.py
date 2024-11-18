import argparse
import os
from pathlib import Path

from gtts import gTTS

SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'pl': 'Polish',
    'ru': 'Russian',
    'nl': 'Dutch',
    'cs': 'Czech',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese',
    'ar': 'Arabic',
    'hi': 'Hindi'
}


def text_to_speech(text: str, lang: str, output_path: str) -> str:
    """
    Convert text to speech using Google Text-to-Speech.

    Args:
        text: The text to convert to speech
        lang: Language code (e.g., 'es' for Spanish, 'en' for English)
        output_path: Full path for the output MP3 file

    Returns:
        Path to the generated audio file
    """
    try:
        # Verify language is supported
        if lang not in SUPPORTED_LANGUAGES:
            raise ValueError(
                f"Language code '{lang}' is not supported. Supported languages: {', '.join(f'{k} ({v})' for k, v in SUPPORTED_LANGUAGES.items())}")

        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir:
            Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Generate speech using specified language
        tts = gTTS(text=text, lang=lang, slow=False)

        # Save the audio file
        tts.save(output_path)
        print(f"Successfully generated {SUPPORTED_LANGUAGES[lang]} audio file: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error generating audio: {str(e)}")
        return None


def read_text_file(file_path: str) -> str:
    """Read text from a file."""
    if not file_path.endswith('.txt'):
        raise ValueError("Input file must have .txt extension")

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None


def list_supported_languages():
    """Print a formatted list of supported languages."""
    print("\nSupported Languages:")
    print("-------------------")
    for code, name in sorted(SUPPORTED_LANGUAGES.items()):
        print(f"{code}: {name}")


def validate_output_file(output_path: str):
    """Validate output file path."""
    if not output_path.endswith('.mp3'):
        raise ValueError("Output file must have .mp3 extension")

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir:
        Path(output_dir).mkdir(parents=True, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description='Convert text file to speech in multiple languages')
    parser.add_argument('--input-file', '-i', required=True,
                        help='Path to input text file (.txt)')
    parser.add_argument('--output-file', '-o', required=True,
                        help='Path to output audio file (.mp3)')
    parser.add_argument('--language', '-l', default='es',
                        help='Language code (e.g., es, en, fr). Use --list-languages to see all options')
    parser.add_argument('--list-languages', action='store_true',
                        help='List all supported languages and their codes')

    args = parser.parse_args()

    # Show supported languages if requested
    if args.list_languages:
        list_supported_languages()
        return

    try:
        # Validate input file
        if not os.path.isfile(args.input_file):
            raise FileNotFoundError(f"Input file not found: {args.input_file}")

        # Read input text
        text = read_text_file(args.input_file)
        if text is None:
            return

        # Validate output file
        validate_output_file(args.output_file)

        # Generate audio
        filepath = text_to_speech(text, args.language, args.output_file)
        if filepath:
            print(f"\nAudio file generated at: {os.path.abspath(filepath)}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
