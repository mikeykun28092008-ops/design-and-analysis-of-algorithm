from math import hypot

def closest_pair(points):
    """Return (minimum distance, pair of points); O(n log^2 n) version."""
    if len(points) < 2: raise ValueError("At least two points are required")
    pts=sorted(points)
    def solve(px):
        n=len(px)
        if n<=3:
            best=(float("inf"), None)
            for i in range(n):
                for j in range(i+1,n):
                    d=hypot(px[i][0]-px[j][0], px[i][1]-px[j][1])
                    if d<best[0]: best=(d,(px[i],px[j]))
            return best
        mid=n//2; midx=px[mid][0]
        left=solve(px[:mid]); right=solve(px[mid:])
        best=left if left[0]<right[0] else right
        strip=[p for p in px if abs(p[0]-midx)<best[0]]
        strip.sort(key=lambda p:p[1])
        for i in range(len(strip)):
            for j in range(i+1,min(i+8,len(strip))):
                d=hypot(strip[i][0]-strip[j][0],strip[i][1]-strip[j][1])
                if d<best[0]: best=(d,(strip[i],strip[j]))
        return best
    return solve(pts)

if __name__ == "__main__":
    print(closest_pair([(2,3),(12,30),(40,50),(5,1),(12,10),(3,4)]))
