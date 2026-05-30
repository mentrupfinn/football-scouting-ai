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

def filter(df, position_group, exclude = False):
    position_cols = POSITION_GROUPS[position_group]
    if exclude:
        return df[~df[position_cols].any(axis=1)]
    return df[df[position_cols].any(axis=1)]