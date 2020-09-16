import abjad

def barline(style):
    """
    Makes a literal barline
    """
    if (style == "|.") or (style == "||") or (stlye == "|!"):
        return abjad.LilyPondLiteral(f"\\bar \"{style}\"", "after")
    else:
        ValueError("choose another style of barline")

def repeat(style):
    if (style == ".|:") or (style == ":|.|:") or (style == ":|."):
        return abjad.LilyPondLiteral(f"\\bar \"{style}\"", "after")
    else:
        ValueError("choose another style of barline")
