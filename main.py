from dotenv import load_dotenv

from gigachat.exceptions import GigaChatException

from chat import Client, ContentError


def main() -> None:
    chat = Client() # API key loads automaticly
    while 1: # waiting for KeyboardInterrupt
        try:
            response = chat.send(input(": "))
            print(f": {response}")
        except GigaChatException as e:
            print(f"GigaChatException: {e}")
        except ContentError as e:
            print(f"ContentError: Непросматриваемый контент ответа: {e.message}")


if __name__ == '__main__':
    load_dotenv()
    try:
        main()
    except KeyboardInterrupt:
        print(" - завершение работы программы.")
