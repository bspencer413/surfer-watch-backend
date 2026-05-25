"""
WSL 2026 Championship Tour static data
======================================
Source: worldsurfleague.com press releases + en.wikipedia.org/wiki/2026_World_Surf_League
Last updated: 2026-05-25 (Surfer Watch v0.2)

This module provides:
  SCHEDULE_2026  -- the 12 CT events with dates and locations
  ROSTER_2026    -- confirmed competitors (men + women) for the 2026 CT season

Used by:
  - Next-event lookup on the saved-surfer card
  - Multi-surfer detection in news articles (meet-recap inference)

Maintenance:
  Update once per year when WSL announces the new season.
  TBC slots will fill in as WSL confirms Challenger Series qualifiers.
"""

from datetime import date


# ---------------------------------------------------------------------------
# SCHEDULE
# ---------------------------------------------------------------------------
# 12 events, April through December 2026.
# Stops 1-9 are regular-season events (36 men, 24 women).
# Stops 10-11 are postseason (24 men, 16 women).
# Stop 12 (Pipe Masters) brings full rosters back for the title decider.

SCHEDULE_2026 = [
    {
        "stop": 1,
        "name": "Rip Curl Pro Bells Beach",
        "location": "Bells Beach, Victoria, Australia",
        "start": date(2026, 4, 1),
        "end": date(2026, 4, 11),
        "phase": "regular",
    },
    {
        "stop": 2,
        "name": "Western Australia Margaret River Pro",
        "location": "Margaret River, Western Australia, Australia",
        "start": date(2026, 4, 17),
        "end": date(2026, 4, 27),
        "phase": "regular",
    },
    {
        "stop": 3,
        "name": "Bonsoy Gold Coast Pro",
        "location": "Snapper Rocks, Queensland, Australia",
        "start": date(2026, 5, 2),
        "end": date(2026, 5, 12),
        "phase": "regular",
    },
    {
        "stop": 4,
        "name": "Corona Cero New Zealand Pro",
        "location": "Raglan, New Zealand",
        "start": date(2026, 5, 15),
        "end": date(2026, 5, 25),
        "phase": "regular",
    },
    {
        "stop": 5,
        "name": "Surf City El Salvador Pro",
        "location": "Punta Roca, La Libertad, El Salvador",
        "start": date(2026, 6, 5),
        "end": date(2026, 6, 15),
        "phase": "regular",
    },
    {
        "stop": 6,
        "name": "VIVO Rio Pro",
        "location": "Saquarema, Rio de Janeiro, Brazil",
        "start": date(2026, 6, 19),
        "end": date(2026, 6, 27),
        "phase": "regular",
    },
    {
        "stop": 7,
        "name": "Lexus Tahiti Pro",
        "location": "Teahupo'o, Tahiti, French Polynesia",
        "start": date(2026, 8, 8),
        "end": date(2026, 8, 18),
        "phase": "regular",
    },
    {
        "stop": 8,
        "name": "Corona Fiji Pro",
        "location": "Cloudbreak, Tavarua, Fiji",
        "start": date(2026, 8, 25),
        "end": date(2026, 9, 4),
        "phase": "regular",
    },
    {
        "stop": 9,
        "name": "Lexus Trestles Pro",
        "location": "Lower Trestles, San Clemente, California, USA",
        "start": date(2026, 9, 11),
        "end": date(2026, 9, 20),
        "phase": "regular",
    },
    {
        "stop": 10,
        "name": "Surf Abu Dhabi Pro",
        "location": "Hudayriat Island, Abu Dhabi, UAE",
        "start": date(2026, 10, 14),
        "end": date(2026, 10, 18),
        "phase": "postseason",
    },
    {
        "stop": 11,
        "name": "MEO Rip Curl Pro Portugal",
        "location": "Supertubos, Peniche, Portugal",
        "start": date(2026, 10, 22),
        "end": date(2026, 11, 1),
        "phase": "postseason",
    },
    {
        "stop": 12,
        "name": "Lexus Pipe Pro",
        "location": "Banzai Pipeline, Oahu, Hawaii, USA",
        "start": date(2026, 12, 8),
        "end": date(2026, 12, 20),
        "phase": "finale",
    },
]


# ---------------------------------------------------------------------------
# ROSTER
# ---------------------------------------------------------------------------
# Each surfer dict has:
#   "name"          canonical display name (used in Surfer Watch)
#   "search_terms"  list of name variants for substring matching in news text
#                   (includes accented forms, common nicknames where applicable)
#   "country"       three-letter country code (display only)
#   "status"        qualifier | challenger | wildcard | event_wildcard
#
# Status values:
#   "qualifier"       qualified from 2025 CT rankings
#   "challenger"      qualified from 2025 Challenger Series
#   "wildcard"        WSL season wildcard
#   "event_wildcard"  event-specific wildcard (no ranking points)
#
# TBC slots from WSL not yet filled. Add them here as they're announced.

ROSTER_2026 = {
    "men": [
        # Qualifiers from 2025 Championship Tour (top 22)
        {"name": "Yago Dora", "search_terms": ["Yago Dora"], "country": "BRA", "status": "qualifier"},
        {"name": "Griffin Colapinto", "search_terms": ["Griffin Colapinto"], "country": "USA", "status": "qualifier"},
        {"name": "Jordy Smith", "search_terms": ["Jordy Smith"], "country": "RSA", "status": "qualifier"},
        {"name": "Italo Ferreira", "search_terms": ["Italo Ferreira", "\u00cdtalo Ferreira"], "country": "BRA", "status": "qualifier"},
        {"name": "Jack Robinson", "search_terms": ["Jack Robinson"], "country": "AUS", "status": "qualifier"},
        {"name": "Ethan Ewing", "search_terms": ["Ethan Ewing"], "country": "AUS", "status": "qualifier"},
        {"name": "Kanoa Igarashi", "search_terms": ["Kanoa Igarashi"], "country": "JPN", "status": "qualifier"},
        {"name": "Filipe Toledo", "search_terms": ["Filipe Toledo"], "country": "BRA", "status": "qualifier"},
        {"name": "Leonardo Fioravanti", "search_terms": ["Leonardo Fioravanti"], "country": "ITA", "status": "qualifier"},
        {"name": "Cole Houshmand", "search_terms": ["Cole Houshmand"], "country": "USA", "status": "qualifier"},
        {"name": "Barron Mamiya", "search_terms": ["Barron Mamiya"], "country": "HAW", "status": "qualifier"},
        {"name": "Connor O'Leary", "search_terms": ["Connor O'Leary", "Connor OLeary"], "country": "JPN", "status": "qualifier"},
        {"name": "Miguel Pupo", "search_terms": ["Miguel Pupo"], "country": "BRA", "status": "qualifier"},
        {"name": "Jake Marshall", "search_terms": ["Jake Marshall"], "country": "USA", "status": "qualifier"},
        {"name": "Crosby Colapinto", "search_terms": ["Crosby Colapinto"], "country": "USA", "status": "qualifier"},
        {"name": "Marco Mignot", "search_terms": ["Marco Mignot"], "country": "FRA", "status": "qualifier"},
        {"name": "Joao Chianca", "search_terms": ["Joao Chianca", "Jo\u00e3o Chianca"], "country": "BRA", "status": "qualifier"},
        {"name": "Joel Vaughan", "search_terms": ["Joel Vaughan"], "country": "AUS", "status": "qualifier"},
        {"name": "Alan Cleland Jr.", "search_terms": ["Alan Cleland", "Alan Cleland Jr."], "country": "MEX", "status": "qualifier"},
        {"name": "Rio Waida", "search_terms": ["Rio Waida"], "country": "INA", "status": "qualifier"},
        {"name": "Seth Moniz", "search_terms": ["Seth Moniz"], "country": "HAW", "status": "qualifier"},
        {"name": "Alejo Muniz", "search_terms": ["Alejo Muniz", "Alejo Mu\u00f1iz"], "country": "BRA", "status": "qualifier"},

        # Qualifiers from 2025 Challenger Series (1 confirmed, 9 TBC)
        {"name": "Eli Hanneman", "search_terms": ["Eli Hanneman"], "country": "USA", "status": "challenger"},
        # TBC: 9 more male Challenger Series qualifiers

        # Season Wildcards
        {"name": "Gabriel Medina", "search_terms": ["Gabriel Medina"], "country": "BRA", "status": "wildcard"},
        {"name": "Ramzi Boukhiam", "search_terms": ["Ramzi Boukhiam"], "country": "MAR", "status": "wildcard"},

        # Event wildcards (no ranking points, but tracked for news mentions)
        {"name": "Dane Henry", "search_terms": ["Dane Henry"], "country": "AUS", "status": "event_wildcard"},
    ],
    "women": [
        # Qualifiers from 2025 Championship Tour (top 14)
        {"name": "Molly Picklum", "search_terms": ["Molly Picklum"], "country": "AUS", "status": "qualifier"},
        {"name": "Caroline Marks", "search_terms": ["Caroline Marks"], "country": "USA", "status": "qualifier"},
        {"name": "Gabriela Bryan", "search_terms": ["Gabriela Bryan"], "country": "HAW", "status": "qualifier"},
        {"name": "Caitlin Simmers", "search_terms": ["Caitlin Simmers"], "country": "USA", "status": "qualifier"},
        {"name": "Bettylou Sakura Johnson", "search_terms": ["Bettylou Sakura Johnson"], "country": "HAW", "status": "qualifier"},
        {"name": "Isabella Nichols", "search_terms": ["Isabella Nichols"], "country": "AUS", "status": "qualifier"},
        {"name": "Tyler Wright", "search_terms": ["Tyler Wright"], "country": "AUS", "status": "qualifier"},
        {"name": "Erin Brooks", "search_terms": ["Erin Brooks"], "country": "CAN", "status": "qualifier"},
        {"name": "Lakey Peterson", "search_terms": ["Lakey Peterson"], "country": "USA", "status": "qualifier"},
        {"name": "Luana Silva", "search_terms": ["Luana Silva"], "country": "BRA", "status": "qualifier"},
        {"name": "Sawyer Lindblad", "search_terms": ["Sawyer Lindblad"], "country": "USA", "status": "qualifier"},
        {"name": "Vahine Fierro", "search_terms": ["Vahine Fierro"], "country": "FRA", "status": "qualifier"},
        {"name": "Bella Kenworthy", "search_terms": ["Bella Kenworthy"], "country": "USA", "status": "qualifier"},
        {"name": "Brisa Hennessy", "search_terms": ["Brisa Hennessy"], "country": "CRC", "status": "qualifier"},

        # Qualifiers from 2025 Challenger Series (4 confirmed, 3 TBC)
        {"name": "Yolanda Hopkins", "search_terms": ["Yolanda Hopkins"], "country": "POR", "status": "challenger"},
        {"name": "Tya Zebrowski", "search_terms": ["Tya Zebrowski"], "country": "FRA", "status": "challenger"},
        {"name": "Sally Fitzgibbons", "search_terms": ["Sally Fitzgibbons"], "country": "AUS", "status": "challenger"},
        {"name": "Francisca Veselko", "search_terms": ["Francisca Veselko"], "country": "POR", "status": "challenger"},
        # TBC: 3 more female Challenger Series qualifiers

        # Season Wildcards
        {"name": "Stephanie Gilmore", "search_terms": ["Stephanie Gilmore", "Steph Gilmore"], "country": "AUS", "status": "wildcard"},
        {"name": "Carissa Moore", "search_terms": ["Carissa Moore"], "country": "HAW", "status": "wildcard"},
    ],
}


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def all_surfers():
    """Flat list of all roster surfers (men + women combined)."""
    return ROSTER_2026["men"] + ROSTER_2026["women"]


def all_search_terms():
    """
    Flat list of every search term across the roster, paired with the
    canonical surfer name. Used for substring detection in news article text.

    Returns: list of (search_term, canonical_name) tuples
    """
    pairs = []
    for surfer in all_surfers():
        for term in surfer["search_terms"]:
            pairs.append((term, surfer["name"]))
    return pairs


def is_on_tour(name):
    """Return True if the given name is on the 2026 CT roster (any tier)."""
    name_lower = name.strip().lower()
    for surfer in all_surfers():
        if surfer["name"].lower() == name_lower:
            return True
        for term in surfer["search_terms"]:
            if term.lower() == name_lower:
                return True
    return False


def next_event(today=None):
    """
    Return the next upcoming CT event whose start date is on or after today.
    Returns None if the season is over.
    """
    if today is None:
        today = date.today()
    for event in SCHEDULE_2026:
        if event["end"] >= today:
            return event
    return None


def event_for_date(d):
    """
    Return the CT event whose contest window contains date d, or None.
    Useful for cross-referencing news article publish dates with events.
    """
    for event in SCHEDULE_2026:
        if event["start"] <= d <= event["end"]:
            return event
    return None


def detect_surfers_in_text(text):
    """
    Scan article text for mentions of any roster surfers.
    Returns a list of canonical surfer names found (deduplicated, in roster order).

    This is the core of the meet-recap inference:
      - If detect_surfers_in_text(article) returns 2+ names,
        the article is likely a meet recap.
    """
    found = []
    seen = set()
    for term, canonical in all_search_terms():
        if term in text and canonical not in seen:
            found.append(canonical)
            seen.add(canonical)
    return found
