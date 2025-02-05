# app.py
def add_numbers(a, b):
    return a - b  # ❌ Incorrect logic (should be `a + b`)

if __name__ == "__main__":
    print(add_numbers(2, 3))  # This will print -1 instead of 5
