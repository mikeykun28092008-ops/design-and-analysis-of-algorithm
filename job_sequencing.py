def job_sequencing(jobs):
    """jobs are (job_id, deadline, profit); assumes unit-time jobs."""
    jobs=sorted(jobs,key=lambda x:x[2],reverse=True)
    slots=[None]*(max((d for _,d,_ in jobs),default=0)+1)
    total=0
    for job_id,deadline,profit in jobs:
        for t in range(min(deadline,len(slots)-1),0,-1):
            if slots[t] is None:
                slots[t]=job_id; total+=profit; break
    return [x for x in slots[1:] if x is not None],total

if __name__ == "__main__":
    print(job_sequencing([("a",2,100),("b",1,19),("c",2,27),("d",1,25),("e",3,15)]))
