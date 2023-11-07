class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(dist)
        arrival_times = [(dist[i] + speed[i] - 1) // speed[i] for i in range(n)]
        arrival_times.sort()  # Sort the monsters by their arrival times.

        eliminated = 0
        time = 0

        for i in range(n):
            if arrival_times[i] > time:
                # You can eliminate the monster at this time.
                eliminated += 1
                time += 1  # Wait for one minute for your weapon to charge.
            else:
                # You lost as the monster reached the city exactly when your weapon was charged.
                break

        return eliminated
