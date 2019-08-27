from collections import deque


def call(pushed, popped):
    popped = deque(popped)
    stack = []

    for i in pushed:
        stack.append(i)
        while len(stack) and len(popped) and stack[-1] == popped[0]:
            stack.pop()
            popped.popleft()

    while len(stack) and len(popped) and stack[-1] == popped[0]:
        stack.pop()
        popped.popleft()

    return not stack


if __name__ == "__main__":
    print(call([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
