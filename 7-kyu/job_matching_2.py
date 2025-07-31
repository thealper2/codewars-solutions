def match(job, candidates):
    matched_candidates = []
    for candidate in candidates:
        equity_ok = not candidate["desires_equity"] or job["equity_max"] > 0
        job_locations = set(job["locations"])
        candidate_locations = {candidate["current_location"]}.union(
            set(candidate["desired_locations"])
        )
        location_ok = not job_locations.isdisjoint(candidate_locations)

        if equity_ok and location_ok:
            matched_candidates.append(candidate)
    return matched_candidates
