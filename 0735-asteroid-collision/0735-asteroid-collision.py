class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def will_collide(a, b):
            return a>0 and b<0
        
        def collide(a, b):
            if not will_collide(a,b): return [a,b]
            if a==-b: return []
            return [max([a,b], key=abs)]
        
        s = []
        for x in asteroids:
            s.append(x)
            while len(s)>1 and will_collide(*s[-2:]):
                b,a = s.pop(), s.pop()
                s.extend(collide(a, b))
        return s