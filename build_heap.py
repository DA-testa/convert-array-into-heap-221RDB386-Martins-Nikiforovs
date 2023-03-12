# python3


def build_heap(data):
    swap = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(len(data) // 2 - 1, -1, -1):
        current_node = i

        while True:
            child_node = current_node * 2 + 1
            if child_node >= len(data):
                break
            if child_node + 1 < len(data) and data[child_node + 1] < data[child_node]:
                child_node += 1
            if data[current_node] < data[child_node]:
                break
            swap.append((current_node, child_node))
            data[child_node], data[current_node] = data[current_node], data[child_node]
            current_node = child_node
    return swap


def main():
  
  # TODO : add input and corresponding checks
  # add another input for I or F
  # first two tests are from keyboard, third test is from a file
  inpt = input()
  if "F" in inpt:
    fileName = input()
    if "a" not in fileName:
      with open(str(fileName), mode="r") as file:
        n = int(file.readline())
        data = list(map(int, file.readline().split()))
    else:
      print("error")
  elif "I" in inpt:
    n = int(input())
    data = list(map(int, input().split()))
  else:
    print("Input error")
  assert len(data) == n
  # checks if lenght of data is the same as the said lenght

  
  # calls function to assess the data 
  # and give back all swaps
  swaps = build_heap(data)
  
  # TODO: output how many swaps were made, 
  # this number should be less than 4n (less than 4*len(data))

  
  # output all swaps
  print("swaps")
  print(len(swaps))
  for i, j in swaps:
    print(i, j)


if __name__ == "__main__":
  main()
# 221RDB386 Mārtiņš Nikiforovs 11.grupa
