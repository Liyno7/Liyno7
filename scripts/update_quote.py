import random
import re
import pathlib

QUOTES = [
    ("The world is not beautiful, therefore it is.", "Kino's Journey"),
    ("If you don't take risks, you can't create a future.", "One Piece — Monkey D. Luffy"),
    ("Whatever you lose, you'll find it again. But what you throw away you'll never get back.", "Fullmetal Alchemist — Kenny"),
    ("A lesson without pain is meaningless.", "Fullmetal Alchemist — Edward Elric"),
    ("Power comes in response to a need, not a desire.", "Dragon Ball Z — Goku"),
    ("It's not the face that makes someone a monster; it's the choices they make with their lives.", "Naruto — Naruto Uzumaki"),
    ("People's lives don't end when they die. It ends when they lose faith.", "Naruto — Itachi Uchiha"),
    ("The moment you think of giving up, think of the reason why you held on so long.", "Naruto"),
    ("If you don't like your destiny, don't accept it.", "Naruto — Naruto Uzumaki"),
    ("Hard work is worthless for those that don't believe in themselves.", "Naruto — Naruto Uzumaki"),
    ("I'll leave tomorrow's problems to tomorrow's me.", "Fruits Basket — Kyo Sohma"),
    ("Fear is not evil. It tells you what your weakness is.", "Fairy Tail — Gildarts Clive"),
    ("No matter how deep the night, it always turns to day, eventually.", "Batman Ninja"),
    ("Whatever happens, happens.", "Cowboy Bebop — Spike Spiegel"),
    ("I'm gonna be the next Hokage, believe it!", "Naruto — Naruto Uzumaki"),
    ("The world isn't perfect, but it's there for us doing the best it can.", "Fullmetal Alchemist"),
    ("A person grows up when he's able to overcome hardships.", "Naruto — Jiraiya"),
    ("Being alone is more painful than getting hurt.", "Naruto — Naruto Uzumaki"),
    ("You should enjoy the little detours to the fullest, because that's where you'll find the things more important than what you want.", "Ging Freecss — Hunter x Hunter"),
    ("Sometimes the questions are complicated and the answers are simple.", "Dr. Seuss (widely quoted in anime fandom)"),
]


def main():
    quote, source = random.choice(QUOTES)
    block = f'💬 *"{quote}"*\n— {source}'

    readme_path = pathlib.Path("README.md")
    text = readme_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r"(<!--START_SECTION:quote-->)(.*?)(<!--END_SECTION:quote-->)",
        re.DOTALL,
    )

    new_text, count = pattern.subn(
        lambda m: f"{m.group(1)}\n{block}\n{m.group(3)}",
        text,
    )

    if count == 0:
        print("No quote markers found in README.md — skipping.")
        return

    readme_path.write_text(new_text, encoding="utf-8")
    print(f"Updated quote: {quote} — {source}")


if __name__ == "__main__":
    main()
