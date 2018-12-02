s = set()
with open("task_input") as f:
  for line in f.read().splitlines():
    for i, _ in enumerate(line):
      new_input = line[:i] + "#" + line[i+1:len(line)]
      old_length = len(s)
      s.add(new_input)
      if len(s) == old_length:
        print(line[:i] + line[i+1:len(line)])
        exit(0)
