def add(A, B):
    n = len(A)
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]

def standard_multiply(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n <= 2: return standard_multiply(A, B)
    m = n//2
    a11=[r[:m] for r in A[:m]]; a12=[r[m:] for r in A[:m]]
    a21=[r[:m] for r in A[m:]]; a22=[r[m:] for r in A[m:]]
    b11=[r[:m] for r in B[:m]]; b12=[r[m:] for r in B[:m]]
    b21=[r[:m] for r in B[m:]]; b22=[r[m:] for r in B[m:]]
    p1=strassen(add(a11,a22), add(b11,b22))
    p2=strassen(add(a21,a22), b11)
    p3=strassen(a11, sub(b12,b22))
    p4=strassen(a22, sub(b21,b11))
    p5=strassen(add(a11,a12), b22)
    p6=strassen(sub(a21,a11), add(b11,b12))
    p7=strassen(sub(a12,a22), add(b21,b22))
    c11=add(sub(add(p1,p4),p5),p7); c12=add(p3,p5)
    c21=add(p2,p4); c22=add(sub(add(p1,p3),p2),p6)
    return [c11[i]+c12[i] for i in range(m)] + [c21[i]+c22[i] for i in range(m)]

def strassen_multiply(A, B):
    """Square matrices of equal size; pads to the next power of two."""
    if not A or len(A) != len(A[0]) or len(B) != len(B[0]) or len(A) != len(B):
        raise ValueError("Matrices must be square and have equal dimensions")
    n=len(A); size=1
    while size<n: size*=2
    X=[row[:] + [0]*(size-n) for row in A] + [[0]*size for _ in range(size-n)]
    Y=[row[:] + [0]*(size-n) for row in B] + [[0]*size for _ in range(size-n)]
    C=strassen(X,Y)
    return [row[:n] for row in C[:n]]

if __name__ == "__main__":
    print(strassen_multiply([[1,2],[3,4]], [[5,6],[7,8]]))
