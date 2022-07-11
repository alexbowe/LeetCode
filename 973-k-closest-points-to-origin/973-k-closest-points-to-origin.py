class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def d(x):
            return x[0]**2 + x[1]**2
        
        def choose_pivot(xs, left, right, k):
            if right-left+1 < 3:
                return right
            mid = left + (right - left)//2
            return sorted([left, mid, right], key=lambda i:k(xs[i]))[1]
        
        def partition(xs, left, right, key=lambda x:x):
            p = choose_pivot(xs, left, right, key)
            pivot_value = key(xs[p])
            xs[right], xs[p] = xs[p], xs[right]
            
            store = left
            # swap pivot and store?
            for i in range(left,right):
                if key(xs[i]) <= pivot_value:
                    xs[store], xs[i] = xs[i], xs[store]
                    store+=1
            xs[store], xs[right] = xs[right], xs[store]
            return store
        
        def quickselect(xs, k, key=lambda x:x):
            left, right = 0, len(xs)-1
            while left < right:
                p = partition(xs, left, right, key)
                if p == k-1: break
                if p < k-1:
                    left = p+1
                if k-1 < p:
                    right = p-1
            return xs[:k]
        
        return quickselect(points, k, key=d)