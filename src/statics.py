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
    "xa/90",     
    "vorl/90",     
    "pr_pässe/90",
    "e_pä/90",     
    "entp(s)/90",  
    "ps_a/90",    
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
    "zwk/90",
    "prserf/90",
    "prsv/90",
    "vek/90"
]

goalkeeping_features = [
    "xg_verh/90",
    "gtor/90",
    "zu0/90",
    "paraden/90"
]

POSITION_GROUPS = {
    "TW": ["TW(Z)"],
    "IV": ["V(Z)"],
    "AV": ["V(L)", "V(R)", "FV(L)", "FV(R)"],
    "DM": ["DM(Z)"],
    "ZM": ["M(L)", "M(Z)", "M(R)"],
    "OM": ["OM(Z)"],
    "Flg": ["OM(L)", "OM(R)"],
    "ST": ["ST(Z)"]
}

TW_FEATURES = [
    "xg_verh/90",
    "paraden/90",
    "zu0/90",
    "ps_a/90",
    "pr_pässe/90"
]

IV_FEATURES = [
    "abb/90",
    "blk/90",
    "klär/90",
    "ent_zwk/90",
    "kopf_g/90",
    "pr_pässe/90",
    "ps_a/90",
    "ballgew/90"
]

AV_FEATURES = [
    "xa/90",
    "vorl/90",
    "drb/90",
    "ang_fla/90",
    "pr_pässe/90",
    "ballgew/90",
    "sprints/90",
    "lauf/90"
]

DM_FEATURES = [
    "ballgew/90",
    "abb/90",
    "ent_zwk/90",
    "pr_pässe/90",
    "ps_a/90",
    "e_pä/90",
    "prserf/90",
    "lauf/90"
]

ZM_FEATURES = [
    "xa/90",
    "pr_pässe/90",
    "e_pä/90",
    "drb/90",
    "ballgew/90",
    "lauf/90",
    "sch/90",
    "prserf/90"
]

OM_FEATURES = [
    "xg/90",
    "xa/90",
    "drb/90",
    "e_pä/90",
    "vorl/90",
    "sch/90",
    "ang_fla/90",
    "ballverl/90"
]

FLG_FEATURES = [
    "xg/90",
    "xa/90",
    "drb/90",
    "ang_fla/90",
    "vorl/90",
    "sch/90",
    "sprints/90",
    "lauf/90"
]

ST_FEATURES = [
    "xg/90",
    "tor/90",
    "sch/90",
    "xg/schuss",
    "kopf_g/90",
    "drb/90",
    "ballverl/90",
    "prserf/90"
]

feature_sets = [
    (TW_FEATURES, POSITION_GROUPS["TW"]),
    (IV_FEATURES, POSITION_GROUPS["IV"]),
    (AV_FEATURES, POSITION_GROUPS["AV"]),
    (DM_FEATURES, POSITION_GROUPS["DM"]),
    (ZM_FEATURES, POSITION_GROUPS["ZM"]),
    (OM_FEATURES, POSITION_GROUPS["OM"]),
    (FLG_FEATURES, POSITION_GROUPS["Flg"]),
    (ST_FEATURES, POSITION_GROUPS["ST"])
    ]