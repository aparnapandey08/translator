from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using MyMemory Translator.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    print(f"Translation response: '{english_text}' -> '{french_text}'")
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using MyMemory Translator.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    print(f"Translation response: '{french_text}' -> '{english_text}'")
    return english_text