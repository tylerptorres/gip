def execute(s1, s2):
    s1_pointer, s2_pointer = len(s1)-1, len(s2)-1

    while s1_pointer >= 0 and s2_pointer >= 0:
        char1 = s1[]



    return True


def build_frequency_array(arr, s):



if __name__ == "__main__":
    print(execute("xy#z", "xzz#"))
    print(execute("xy#z", "xyz#"))
    print(execute("xp#", "xyz##"))
    print(execute("xywrrmp", "xywrrmu#p"))

    # x y # z
    # x z z #

    """ 
    Roadmap
        1. If we have a letter, we're going to increment its count in the array
        2. while we have a backspace, 
            - add + 1 to back spaces
            - decrement pointer
        3. while backspaces > 0 and left > 0, move pointer left
        4. return arr1 == arr2
     """
