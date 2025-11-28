#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char *WORDLIST[] = {
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
};
static const size_t WORDLIST_SIZE = sizeof(WORDLIST) / sizeof(WORDLIST[0]);

static int find_index(const char *word) {
    for (size_t i = 0; i < WORDLIST_SIZE; ++i) {
        if (strcmp(word, WORDLIST[i]) == 0) return (int)i;
    }
    return -1;
}

unsigned char *decode_shellcode(const char *encoded, size_t *out_len) {
    if (!encoded) { *out_len = 0; return NULL; }

    // duplicate input because strtok modifies it
    char *buf = _strdup(encoded);
    if (!buf) { *out_len = 0; return NULL; }

    // first pass: count tokens
    size_t count = 0;
    char *p = buf;
    char *tok = strtok(p, " \t\r\n");
    while (tok) {
        ++count;
        tok = strtok(NULL, " \t\r\n");
    }

    // allocate output buffer
    unsigned char *out = malloc(count ? count : 1);
    if (!out) { free(buf); *out_len = 0; return NULL; }

    // second pass: fill bytes
    strcpy(buf, encoded); // restore original into buf
    size_t idx = 0;
    tok = strtok(buf, " \t\r\n");
    while (tok) {
        int id = find_index(tok);
        if (id < 0) {
            fprintf(stderr, "Word '%s' not found in wordlist\n", tok);
            free(out);
            free(buf);
            *out_len = 0;
            return NULL;
        }
        out[idx++] = (unsigned char)id;
        tok = strtok(NULL, " \t\r\n");
    }

    free(buf);
    *out_len = idx;
    return out;
}

int main(void) {
    const char *encoded = "Aurelion Taliyah Urgot global glass OP Elixir peeling peeling peeling backdoor Swain backdoor so";
    size_t len = 0;
    unsigned char *decoded = decode_shellcode(encoded, &len);
    if (!decoded) return 1;

    // print hex string
    printf("Decoded bytes: ");
    for (size_t i = 0; i < len; ++i) {
        printf("%02x", decoded[i]);
    }
    printf("\n");

    // print comma-separated 0x.. list
    for (size_t i = 0; i < len; ++i) {
        printf("0x%02X", decoded[i]);
        if (i + 1 < len) printf(", ");
    }
    printf("\n");

    free(decoded);
    return 0;
}