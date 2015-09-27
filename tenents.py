from pprint import pprint

def print_file(grouped_dict):
    with open("directory.html", 'w') as f:
        f.write("<html><body>")
        for key in sorted(grouped_dict):
            f.write("<ul>")
            f.write("<h1>" + key + "</h1>")
            tenants_list = grouped_dict[key]
            for tenant in tenants_list:
                f.write("<li>")
                name = tenant["name"]
                suite = tenant["suite"]
                f.write(name + " " + str(suite))
                f.write("</li>")
            f.write("</ul>")


def group_tenants(tenants):
    directory = {}
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in tenants:
        first_letter = item["name"][0].upper()
        if not first_letter.isalpha():
            first_letter = '*'
        if not first_letter in directory:
            directory[first_letter] = []
        directory[first_letter].append(item)
    return directory


def main():
    tenants = [
        {"name": "Kevin Long",
         "suite": 111},
        {"name": "Kay Long",
         "suite": 112},
        {"name": "John Long",
         "suite": 113},
        {"name": "Jack Richards",
         "suite": 211},
        {"name": "Arthur Wright",
         "suite": 212},
        {"name": "abc",
         "suite": 123},
        {"name": "31 flavors",
         "suite": 231},
        {"name": "!@#$%^&*()",
         "suite": 213}
    ]
    grouped_dict = group_tenants(tenants)
    pprint(grouped_dict)
    #Once grouped_dict is grouped properly
    #We will print out the html file here...
    print_file(grouped_dict)


if __name__ == '__main__':
    main()