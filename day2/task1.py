from collections import defaultdict
from enum import Enum

class Warehouse:
  def __init__(self):
    self.doubles = 0
    self.triples = 0

  def parse_file(self, filename: str="task_input"):
    with open(filename) as f:
      for line in f.readlines():
        self.count_duplicates(line=line)

  def count_duplicates(self, line: str):
    d = defaultdict(int)
    for c in line:
      d[c] += 1

    if 2 in d.values():
      self.doubles += 1
    if 3 in d.values():
      self.triples += 1

  def calculate_checksum(self) -> int:
    return self.doubles * self.triples


warehouse = Warehouse()
warehouse.parse_file(filename="task_input")
print(warehouse.calculate_checksum())

