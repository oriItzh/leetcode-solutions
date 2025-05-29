class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        Problem: Push Dominoes; leetcode #838

        There are n dominoes in a line, and we place each domino vertically upright.
        In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
        After each second, each domino that is falling to the left pushes the adjacent domino on the left.
        Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
        When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
        For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

        You are given a string dominoes representing the initial state where:

        dominoes[i] = 'L', if the ith domino has been pushed to the left,
        dominoes[i] = 'R', if the ith domino has been pushed to the right, and
        dominoes[i] = '.', if the ith domino has not been pushed.
        Return a string representing the final state.



        Example 1:

        Input: dominoes = "RR.L"
        Output: "RR.L"
        Explanation: The first domino expends no additional force on the second domino.
        """
        n = len(dominoes)
        distRight = [n] * n
        distLeft = [n] * n

        time = n
        for i in range(n):
            if dominoes[i] == "R":
                time = 0
            elif dominoes[i] == "L":
                time = n
            elif time < n:
                time += 1
            distRight[i] = time

        time = n
        for i in reversed(range(n)):
            if dominoes[i] == "L":
                time = 0
            elif dominoes[i] == "R":
                time = n
            elif time < n:
                time += 1
            distLeft[i] = time

        res = []
        for distL, distR in zip(distLeft, distRight):
            cur = "."
            if distL != distR:
                cur = "R" if distR < distL else "L"
            res.append(cur)

        return "".join(res)
