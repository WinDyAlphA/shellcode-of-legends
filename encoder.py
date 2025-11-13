
WORDLIST = [
    "peeling", "Akshan", "dodge", "bot", "double", "Hue", "nerf", "wards", "Neeko", "Anivia", "instalock", 
    "Quadra", "Leona", "Yasuo", "Kog'Maw", "quadra", "fountain", "Ace", "Kennen", "Legends", "cooldown", "Taric", 
    "Zyra", "Aatrox", "report", "Twitch", "doran's", "Jarvan", "Galio", "riot", "Sion", "Zed", "sustain", "BotRK", 
    "closer", "pls", "Akali", "Dr", "towers", "kench", "roam", "Fiddlesticks", "Blitzcrank", "dive", "Bush", "Karma", 
    "reset", "Sona", "toxic", "Maokai", "wolves", "Morgana", "Caitlyn", "Assassin", "cannon", "Trundle", "quadrakill", 
    "Mordekaiser", "Fate", "Garen", "Elo", "CC", "pisslow", "Zhao", "gap", "backdoor", "Rengar", "auto-attack", "support",
    "ult", "check", "tank", "Taliyah", "ms", "ragequit", "int", "Cho'Gath", "OOM", "bork", "1v1", "so", "Swain", "Ezreal",
    "wraiths", "bruiser", "Jax", "rito", "Vi", "skintimidation", "buffs", "Renekton", "Yi", "golems", "Gragas", "Ornn", 
    "counter", "hue", "penta", "blink", "utility", "Thresh", "Zeri", "Darius", "gank", "Malzahar", "inhibitor", "Shen", 
    "Lillia", "Cassiopeia", "Teemo", "rift", "Ahri", "Kindred", "Viktor", "Diana", "Volibear", "Lag", "fed", "Janna", "summoner", 
    "jungle", "Willump", "kite", "Nocturne", "Kassadin", "Towers", "dragon", "Lissandra", "nexus", "Lux", "overextending", 
    "Urgot", "Sylas", "Sin", "CS", "Wukong", "Mundo", "burst", "ff", "split", "Fiora", "Irelia", "Braum", "ARAM", "creeps", 
    "Inhibitor", "ace", "Master", "Last", "Xayah", "Ryze", "push", "minions", "troll", "Illaoi", "pro", "Brand", "Seraphine", 
    "smurf", "Syndra", "Baron", "Gangplank", "Rell", "masteries", "Pantheon", "of", "Fortune", "Karthus", "escape", "baron", "ADC", 
    "wave", "such", "Sett", "Elise", "Rakan", "Miss", "leash", "ranked", "assassin", "Jinx", "Skintimidation", "Twisted", "Yuumi", 
    "Draven", "and", "Kalista", "Fizz", "Samira", "Annie", "queue", "flash", "Elixir", "ignite", "Gwen", "pill", "DC", "Kha'Zix", "fog", 
    "proc", "Zilean", "war", "Xin", "League", "LeBlanc", "Viego", "ultimate", "ez", "bush", "mana", "Lee", "KS", "esports", "Malphite", 
    "Jhin", "trade", "sol", "Hecarim", "Rek'Sai", "Peeling", "zoning", "Ivern", "pentakill", "Inhib", "Ashe", "chase", "Zac", "lore", 
    "global", "Nidalee", "inhib", "Udyr", "OP", "buff", "Tristana", "Lucian", "Pyke", "Skarner", "Renata", "Rumble", "glass", "bronze", 
    "jukes", "Quinn", "Sivir", "Sejuani", "skillshot", "lane", "Lulu", "Vayne", "Glasc", "hit", "Aurelion", "blue", "overstaying", "map"
]

def encode_shellcode(shellcode: bytes, wordlist=WORDLIST) -> str:
    """
    Prend un shellcode (type bytes) et renvoie une chaîne de mots
    séparés par des espaces.
    Chaque byte b devient wordlist[b].
    """
    if len(wordlist) != 256:
        raise ValueError(f"Wordlist must contain 256 words, got {len(wordlist)}")

    return " ".join(wordlist[b] for b in shellcode)


def main():
    shellcode = bytes([
        0xFC, 0x48, 0x83, 0xE4, 0xF0, 0xE8, 0xC0, 0x00,
        0x00, 0x00, 0x41, 0x51, 0x41, 0x50
    ])

    encoded = encode_shellcode(shellcode)
    print(encoded)


if __name__ == "__main__":
    main()