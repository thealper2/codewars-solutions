import re


def get_users_ids(st):
    ids = st.lower().split(",")
    pattern = r"^[\s#]*uid|#"
    return [re.sub(pattern, "", id).strip() for id in ids]
