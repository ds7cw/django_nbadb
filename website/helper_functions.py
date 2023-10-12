def table_breakdown(page_num: int, rows_per_page: int) -> tuple:
    end_idx = page_num * rows_per_page
    start_idx = end_idx - rows_per_page
    return start_idx, end_idx
