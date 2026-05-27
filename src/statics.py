POSITIONS = [
    "TW(Z)",
    "V(L)", "V(Z)", "V(R)",
    "FV(L)", "DM(Z)", "FV(R)",
    "M(L)", "M(Z)", "M(R)",
    "OM(L)", "OM(Z)", "OM(R)",
    "ST(Z)"
]

POSITION_LAYOUT = {
    "TW(Z)": (0, 0),

    "V(L)": (-2, 1),
    "V(Z)": (0, 1),
    "V(R)": (2, 1),

    "FV(L)": (-2, 2),
    "DM(Z)": (0, 2),
    "FV(R)": (2, 2),

    "M(L)": (-2, 3),
    "M(Z)": (0, 3),
    "M(R)": (2, 3),

    "OM(L)": (-2, 4),
    "OM(Z)": (0, 4),
    "OM(R)": (2, 4),

    "ST(Z)": (0, 5)
}

shooting_features = [
    "xg/90",
    "xg-ohn11/90",
    "tor/90",
    "sch/90",
    "sat/90",
    "xg/schuss",
    "fernschüsse/90"
]

passing_features = [
    "xa/90",          # expected assists → Chance creation
    "vorl/90",        # key passes / assists prep
    "pr_pässe/90",    # progressive passes
    "e_pä/90",        # passes into final third (vermutlich)
    "entp(s)/90",     # passes into penalty area / dangerous zone
    "ps_a/90",        # pass attempts (volumen)
    "ps_v/90",
    "ch/90"
]

crossing_features = [
    "ang_fla/90",
    "ent_kopf/90",
    "vers_fla/90",
    "kopf_g/90",
    "kop_v/90"
]

possession_features = [
    "ballgew/90",
    "ballverl/90",
    "drb/90",
    "sprints/90",
    "lauf/90"
]

defensive_features = [
    "abb/90",
    "ent_zwk/90",
    "blk/90",
    "klär/90",
    "zwk/90"
]

goalkeeping_features = [
    "xg_verh/90",
    "gtor/90",
    "zu0/90",
    "paraden/90"
]

rest_features = [
    "prserf/90",
    "prsv/90",
    "vek/90"
]

POSITION_GROUPS = {
    "TW": {"TW(Z)"},
    "IV": ["V(Z)"],
    "AV": ["V(L)", "V(R)", "FV(L)", "FV(R)"],
    "DM": ["DM(Z)"],
    "ZM": ["M(L)", "M(Z)", "M(R)"],
    "OM": ["OM(Z)"],
    "Flügel": ["OM(L)", "OM(R)"],
    "ST": ["ST(Z)"]
}