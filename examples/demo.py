"""A demo to use the national park library."""

from examples import np_library

import json


def demo():
    """Demo function."""
    library = np_library.NPLibrary()

    # Insert the national park data from a JSON file.
    print("1. Insert national park data from national_parks.json")
    with open("examples/national_parks.json") as np_data:
        parks = json.load(np_data)
        for park in parks:
            park_data = np_library.NPData(name=park["name"],
                                          location=park["location"],
                                          date=park["date"],
                                          area=park["area"])
            library.insert(data=park_data)

    # List all the data.
    print("2. List the inserted data and sort by name")
    library.list_all(sort_type=np_library.SortType.Name)

    # Add a new national park.
    print("3. Add a new national park, Gateway Arch")
    gateway_arch = np_library.NPData(name="Gateway Arch",
                                     location="Missouri",
                                     date="February 22, 2018",
                                     area=193)
    library.insert(data=gateway_arch)

    # Add another one.
    print("4. Add one more national park, Indiana Dunes")
    indiana_dunes = np_library.NPData(name="Indiana Dunes",
                                      location="Missouri",
                                      date="February 22, 2018",
                                      area=15067)
    library.insert(data=indiana_dunes)

    # Check if the new national parks inserted properly.
    print("5. Check if both national parks are inserted properly")
    library.query(name="Gateway Arch").dump()
    library.query(name="Indiana Dunes").dump()

    # Find out the data of Indiana Dunes is not correct.
    print("6. Fix the data of Indiana Dunes")
    correct_indiana_dunes = np_library.NPData(name="Indiana Dunes",
                                              location="Indiana",
                                              date="February 15, 2019",
                                              area=15067)
    library.update(name="Indiana Dunes", data=correct_indiana_dunes)

    # Check again.
    print("7. Check the data of Indiana Dunes again")
    library.query(name="Indiana Dunes").dump()

    # List all.
    print("8. List all the data and sort by name")
    library.list_all(sort_type=np_library.SortType.Name)

    print("9. List all the data and sort by size")
    library.list_all(sort_type=np_library.SortType.Size)

    print("10. List all the data and sort by size decending")
    library.list_all(sort_type=np_library.SortType.Size, ascending=False)

    # Add a fake data to demo delete function.
    print("11. Insert a fake national park data to demo delete function")
    fake = np_library.NPData(name="Fake",
                             location="Earth",
                             date="February 15, 2077",
                             area=12345)
    library.insert(data=fake)

    # Check it.
    print("12. Check the fake national park")
    library.query(name="Fake").dump()

    # Delete it.
    print("13. Delete the fake national park")
    library.delete(name="Fake")

    # Check it.
    print("14. Check if the fake national park is deleted properly")
    try:
        library.query(name="Fake")
    except KeyError:
        print("Fake national park does not exist.")


if __name__ == "__main__":
    demo()
