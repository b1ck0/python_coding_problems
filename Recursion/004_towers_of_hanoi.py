def recursive_towers(n_disks, move_from, move_to, spare_location):
    """
    :param n_disks: number of disks to shift
    :param move_from: tower #
    :param move_to: tower #
    :param spare_location: tower #
    :return:
    """
    if n_disks == 1:
        print(f"moving from {move_from} to {move_to}")
    else:
        recursive_towers(n_disks - 1, move_from, spare_location, move_to)
        recursive_towers(1, move_from, move_to, spare_location)
        recursive_towers(n_disks - 1, spare_location, move_to, move_from)


if __name__ == "__main__":
    recursive_towers(5, 2, 1, 3)
