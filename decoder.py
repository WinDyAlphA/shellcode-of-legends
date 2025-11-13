

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


def decode_shellcode(encoded: str, wordlist=WORDLIST) -> bytes:
    
    word_to_index = {word: index for index, word in enumerate(wordlist)}
    
    words = encoded.split()
    result = []
    
    for word in words:
        if word not in word_to_index:
            raise ValueError(f"Word '{word}' not found in wordlist")
        result.append(word_to_index[word])
    
    return bytes(result)


def main():
    encoded = "Aurelion Taliyah Urgot global glass OP Elixir peeling peeling peeling backdoor Swain backdoor so"
    
    decoded = decode_shellcode(encoded)
    print(f"Decoded bytes: {decoded.hex()}")
    
    shellcode_str = ", ".join(f"0x{b:02X}" for b in decoded)
    print(shellcode_str)

if __name__ == "__main__":
    main()
