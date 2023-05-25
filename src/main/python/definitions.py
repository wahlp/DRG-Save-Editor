# contains constants relating to things like guids, xp_tables, etc.
# global constants


import re


# xp_table[i] = XP needed for level i+1
XP_TABLE: list[int] = [
    0,
    3000,
    7000,
    12000,
    18000,
    25000,
    33000,
    42000,
    52000,
    63000,
    75000,
    88000,
    102000,
    117000,
    132500,
    148500,
    165000,
    182000,
    199500,
    217500,
    236000,
    255000,
    274500,
    294500,
    315000,
]
# ordered list of the promotion ranks (low -> high)
PROMO_RANKS: list[str] = [
    "None",
    "Bronze 1",
    "Bronze 2",
    "Bronze 3",
    "Silver 1",
    "Silver 2",
    "Silver 3",
    "Gold 1",
    "Gold 2",
    "Gold 3",
    "Platinum 1",
    "Platinum 2",
    "Platinum 3",
    "Diamond 1",
    "Diamond 2",
    "Diamond 3",
    "Legendary 1",
    "Legendary 2",
    "Legendary 3",
    "Legendary 3+",
]
MAX_BADGES: int = len(PROMO_RANKS) - 1

# ordered list of player rank titles (low -> high)
RANK_TITLES: list[str] = [
    "Greenbeard",
    "Rock Hauler",
    "Cave Runner",
    "Stone Breaker",
    "Pit Delver",
    "Rookie Miner",
    "Rookie Miner",
    "Authorized Miner",
    "Authorized Miner",
    "Senior Miner",
    "Senior Miner",
    "Professional Miner",
    "Professional Miner",
    "Veteran Miner",
    "Veteran Miner",
    "Expert Miner",
    "Expert Miner",
    "Elite Miner",
    "Elite Miner",
    "Elite Miner",
    "Supreme Miner",
    "Supreme Miner",
    "Supreme Miner",
    "Master Miner",
    "Master Miner",
    "Master Miner",
    "Epic Miner",
    "Epic Miner",
    "Epic Miner",
    "Epic Miner",
    "Legendary Miner",
    "Legendary Miner",
    "Legendary Miner",
    "Legendary Miner",
    "Legendary Miner",
    "Mythic Miner",
    "Mythic Miner",
    "Mythic Miner",
    "Mythic Miner",
    "Mythic Miner",
    "Stone Guard",
    "Stone Guard",
    "Stone Guard",
    "Stone Guard",
    "Stone Guard",
    "Honor Guard",
    "Honor Guard",
    "Honor Guard",
    "Honor Guard",
    "Honor Guard",
    "Iron Guard",
    "Iron Guard",
    "Iron Guard",
    "Iron Guard",
    "Iron Guard",
    "Giant Guard",
    "Giant Guard",
    "Giant Guard",
    "Giant Guard",
    "Giant Guard",
    "Night Carver",
    "Night Carver",
    "Night Carver",
    "Night Carver",
    "Night Carver",
    "Longbeard",
    "Longbeard",
    "Longbeard",
    "Longbeard",
    "Longbeard",
    "Gilded Master",
    "Gilded Master",
    "Gilded Master",
    "Gilded Master",
    "Gilded Master",
]

RESOURCE_GUIDS: dict[str, str] = {
    "yeast": "078548B93232C04085F892E084A74100",
    "starch": "72312204E287BC41815540A0CF881280",
    "barley": "22DAA757AD7A8049891B17EDCC2FE098",
    "bismor": "AF0DC4FE8361BB48B32C92CC97E21DE7",
    "enor": "488D05146F5F754BA3D4610D08C0603E",
    "malt": "41EA550C1D46C54BBE2E9CA5A7ACCB06",
    "umanite": "5F2BCF8347760A42A23B6EDC07C0941D",
    "jadiz": "22BC4F7D07D13E43BFCA81BD9C14B1AF",
    "croppa": "8AA7FB43293A0B49B8BE42FFE068A44C",
    "magnite": "AADED8766C227D408032AFD18D63561E",
    "error": "5828652C9A5DE845A9E2E1B8B463C516",
    "cores": "A10CB2853871FB499AC854A1CDE2202C",
    "data": "99FA526AD87748459498905A278693F6",
    "phazyonite": "67668AAE828FDB48A9111E1B912DBFA4",
}

XP_PER_SEASON_LEVEL: int = 5000

GUID_RE: re.Pattern[str] = re.compile(r".*\(([0-9A-F]*)\)")

SEASON_GUIDS: dict[int, str] = {
    1: "A47D407EC0E4364892CE2E03DE7DF0B3",
    2: "B860B55F1D1BB54D8EE2E41FDA9F5838",
    3: "D8810F6C76D374419AE6A18EF5B3BA26",
}

SEASON_GUID: str = SEASON_GUIDS[3]