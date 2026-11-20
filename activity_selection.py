def activity_selection(activities):
    """activities is a list of (start, finish); returns a maximum-size compatible set."""
    chosen=[]; last_finish=float("-inf")
    for start,finish in sorted(activities,key=lambda x:x[1]):
        if start>=last_finish:
            chosen.append((start,finish)); last_finish=finish
    return chosen

if __name__ == "__main__":
    print(activity_selection([(1,3),(2,5),(4,7),(1,8),(8,9)]))
