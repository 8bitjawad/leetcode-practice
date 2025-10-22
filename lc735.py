class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
#stack = [] asteroids= 5,10,-5 
# stack = [5, 10] asteroids = -5 peek top of stack, if lesser than asteroid, pop, keep popping till stack empty or till top > asteroid
# if negative asteroid < top of stack ignore and continue

        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            
            else:
                while stack and abs(asteroids[i]) > abs(stack[-1]) and stack[-1] > 0:
                        stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroids[i])

                elif abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    continue

                else:
                    continue
                
        return stack

        