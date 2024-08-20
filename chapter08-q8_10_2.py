import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def divide(x1, x2):
    try:
        result = x1 / x2
        return result
    except ZeroDivisionError as e:
        logging.exception("ZeroDivisionError: 割り算の除数がゼロです。")
        raise

if __name__ == "__main__":
    try:
        print(divide(10, 0))
    except ZeroDivisionError:
        print("例外が発生しました。")
