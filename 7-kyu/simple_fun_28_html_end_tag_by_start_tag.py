def html_end_tag_by_start_tag(start_tag):
    tag_name = start_tag.split()[0].strip("<>")
    return f"</{tag_name}>"
