from itertools import cycle

cycle_frequencies = cycle([int(line.rstrip('\n')) for line in open('task_input')])
past_frequencies = set()
current_frequency = 0

for freq in cycle_frequencies:
  past_frequencies.add(current_frequency)
  current_frequency += freq
  if current_frequency in past_frequencies:
    print(current_frequency)
    exit(0)
