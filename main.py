from services.model_service import generate_text
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        generated_text = generate_text(input_text)
        print(generated_text)
    else:
        print("Please provide input text.")