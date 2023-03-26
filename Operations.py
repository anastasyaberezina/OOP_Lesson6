import sys


class Operations():

    def list_relation(self, person_name, relation):
        sorted_relations = []
        for person in person:
            if person_name == person.name:
                for family_member in person.family[relation]:
                    sorted_relations.append(family_member.name)
        for member in sorted(sorted_relations):
            if member != person_name:
                print(member)

    def is_relation(self, person_name_one, person_name_two, relation):
        for person in person:
            if person_name_one == person.name:
                for person_2 in person:
                    if person_name_two == person_2.name:
                        if person_2 in person.family_tree[relation]:
                            print("Yes")
                            return
                        else:
                            print("No")
                            return
        print("No")

    def closest_relation(self, person_two, person_one):
        if person_two in person_one.family["spouse"]:
            print("spouse")
            return
        if person_two in person_one.family["parent"]:
            print("parent")
            return
        if person_two in person_one.family["sibling"]:
            print("sibling")
            return
        if person_two in person_one.family["half-sibling"]:
            print("half-sibling")
            return
        if person_two in person_one.family["ancestor"]:
            print("ancestor")
            return
        if person_two in person_one.family["cousin"]:
            print("cousin")
            return
        else:
            print("Unrelated")
            return

def retrieve_person(person_name):
    for person in person:
        if person.name == person_name:
            return person

    x = person(person_name)
    person.append(x)
    return x

def fileRead():
    op = Operations()
    x = sys.stdin.buffer.read()
    x = str(x, "utf-8")
   

    input_list = x.split("\n")
    text = input_list
    for line in text:
        line.rsplit()
        commands = line.split(" ")

        if commands[0] is "E":
            if len(commands) is 4:
                person_one = retrieve_person(commands[1])
                person_two = retrieve_person(commands[2])
                person_three = retrieve_person(commands[3])
                person_three.add_parents(person_one, person_two)

            if len(commands) is 3:
                person_one = retrieve_person(commands[1])
                person_two = retrieve_person(commands[2])
                person_one.add_spouse(person_two)

        if commands[0] is "W":
            person_one = retrieve_person(commands[2])
            relation = commands[1]
            print("\n" + line)
            op.list_relation(person_one.name, relation)

        if commands[0] is "R":
            person_one = retrieve_person(commands[1])
            person_two = retrieve_person(commands[2])
            print("\n" + line)
            op.closest_relation(person_one, person_two)

        if commands[0] is "X":
            person_one = retrieve_person(commands[1])
            relation = commands[2]
            person_two = retrieve_person(commands[3])
            print("\n" + line)
            op.is_relation(person_one.name, person_two.name, relation)
