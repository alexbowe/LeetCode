class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_squared(x):
            return x[0]**2 + x[1]**2
        
        return sorted(points, key=distance_squared)[:k]
        
        def partition(xs, key, left, right):
            pivot_idx = left
            pivot_value = key(xs[pivot_idx])
            xs[right], xs[pivot_idx] = xs[pivot_idx], xs[right]
            store_idx = left
            for i in range(left, right):
                if key(xs[i]) < pivot_value:
                    xs[i], xs[store_idx] = xs[store_idx], xs[i]
                    store_idx += 1
            xs[right], xs[store_idx] = xs[store_idx], xs[right]
            return store_idx
        
        def quickselect(xs, key, k):
            left, right = 0, len(xs)-1
            while left <= right:
                pivot_idx = partition(xs, key, left, right)
                
                if k == pivot_idx:
                    break
                
                if k < pivot_idx:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
            return xs[:pivot_idx]
        
        return quickselect(points, distance_squared, k)