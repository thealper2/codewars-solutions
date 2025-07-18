def pagination_text(page_number, page_size, total_products):
    start = (page_number - 1) * page_size + 1
    end = min(page_number * page_size, total_products)
    return f"Showing {start} to {end} of {total_products} Products."
