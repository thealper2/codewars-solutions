def zipvalidate(postcode):
    return (
        len(postcode) == 6 and
        postcode.isdigit() and
        postcode[0] not in {'0', '5', '7', '8', '9'}
    )