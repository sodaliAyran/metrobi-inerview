import time
import sys

DISTANCE_BETWEEN_ACHILLES_AND_TURTLE = 32
INITIAL_SPEED_OF_ACHILLES = 8
INITIAL_SPEED_OF_TURTLE = int(INITIAL_SPEED_OF_ACHILLES / 2)

for i in range(100):
    time.sleep(0.4)
    t = int(i % (DISTANCE_BETWEEN_ACHILLES_AND_TURTLE / 4 + 1))
    sys.stdout.write("\r" + ((t) * INITIAL_SPEED_OF_ACHILLES) * "=" + "A" +
    (DISTANCE_BETWEEN_ACHILLES_AND_TURTLE - (t) * INITIAL_SPEED_OF_ACHILLES +
    (t) * INITIAL_SPEED_OF_TURTLE) * "=" + "T" + (DISTANCE_BETWEEN_ACHILLES_AND_TURTLE
     - (t) * INITIAL_SPEED_OF_TURTLE) * "=")
    sys.stdout.flush()
print("\nEnd!")
