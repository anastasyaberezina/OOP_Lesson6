import sys

person_list = []

class Family_tree():

    def __init__(self):
        self.family_tree = {"sibling": [], "parent": [], "half-sibling": [], "cousin": [], "children": [], 'spouse': [],"ancestor": []}

class Person:

    def __init__(self, name):
        self.name = name
        self.family_tree = Family_tree().family_tree

    def add_parents(self, parent_one, parent_two):
        self.family_tree['parent'].append(parent_one)
        if parent_one not in parent_two.family_tree['spouse']:
            parent_two.family_tree['spouse'].append(parent_one)
        self.family_tree['parent'].append(parent_two)
        if parent_two not in parent_one.family_tree['spouse']:
            parent_one.family_tree['spouse'].append(parent_two)

        parent_one.add_children(self)
        parent_two.add_children(self)

        self.add_siblings(parent_one, parent_two)

        if parent_one not in self.family_tree['ancestor']:
            self.family_tree['ancestor'].append(parent_one)
        for ancestor in parent_one.family_tree['ancestor']:
            if ancestor not in self.family_tree['ancestor']:
                self.family_tree['ancestor'].append(ancestor)

        if parent_two not in self.family_tree['ancestor']:
            self.family_tree['ancestor'].append(parent_two)
        for ancestor in parent_two.family_tree['ancestor']:
            if ancestor not in self.family_tree['ancestor']:
                self.family_tree['ancestor'].append(ancestor)

        self.add_cousins(parent_one, parent_two)

    def add_children(self, child):
        self.family_tree['children'].append(child)

    def add_spouse(self, spouse):
        if spouse not in self.family_tree['spouse']:
            self.family_tree['spouse'].append(spouse)
        if self not in spouse.family_tree['spouse']:
            spouse.family_tree['spouse'].append(self)

    def add_siblings(self, parent_one, parent_two):
        for child in parent_one.family_tree['children']:
            if child not in self.family_tree['sibling'] and self.name is not child.name:
                if child in parent_two.family_tree['children']:
                    self.family_tree['sibling'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-sibling'].append(child)
                    if self not in child.family_tree['half-sibling']:
                        child.family_tree['half-sibling'].append(self)

            if self not in child.family_tree['cousin']:
                child.family_tree['cousin'].append(self)
            if child not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(child)

        for child in parent_two.family_tree['children']:
            if child not in self.family_tree['sibling'] and self.name is not child.name:
                if child in parent_one.family_tree['children']:
                    self.family_tree['sibling'].append(child)
                    child.add_siblings(parent_one, parent_two)
                else:
                    self.family_tree['half-sibling'].append(child)
                    if self not in child.family_tree['half-sibling']:
                        child.family_tree['half-sibling'].append(self)

            if self not in child.family_tree['cousin']:
                child.family_tree['cousin'].append(self)
            if child not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(child)

    def add_cousins(self, parent_one, parent_two):
        for p in person_list:
            for ancestor in self.family_tree['ancestor']:
                if ancestor in p.family_tree['ancestor'] and p not in self.family_tree['cousin']:
                    self.family_tree['cousin'].append(p)
                    if self not in p.family_tree['cousin']:
                        p.family_tree['cousin'].append(self)

        for cousin in parent_one.family_tree['cousin']:
            if cousin not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(cousin)
            if self not in cousin.family_tree['cousin']:
                cousin.family_tree['cousin'].append(self)

        for cousin in parent_two.family_tree['cousin']:
            if cousin not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(cousin)
            if self not in cousin.family_tree['cousin']:
                cousin.family_tree['cousin'].append(self)

        for sibling in parent_one.family_tree['sibling']:
            if sibling not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(sibling)
            if self not in sibling.family_tree['cousin']:
                sibling.family_tree['cousin'].append(self)

        for halfsib in parent_one.family_tree['half-sibling']:
            if halfsib not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(halfsib)
            if self not in halfsib.family_tree['cousin']:
                 halfsib.family_tree['cousin'].append(self)

        for sibling in parent_two.family_tree['sibling']:
            if sibling not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(sibling)
            if self not in sibling.family_tree['cousin']:
                sibling.family_tree['cousin'].append(self)

        for halfsib in parent_two.family_tree['half-sibling']:
            if halfsib not in self.family_tree['cousin']:
                self.family_tree['cousin'].append(halfsib)
            if self not in halfsib.family_tree['cousin']:
                halfsib.family_tree['cousin'].append(self)

class Operations():

    def list_relation(self, person_name, relation):
        sorted_relations = []
        for person in person_list:
            if person_name == person.name:
                for family_member in person.family_tree[relation]:
                    sorted_relations.append(family_member.name)
        for member in sorted(sorted_relations):
            if member != person_name:
                print(member)

    def is_relation(self, person_name_one, person_name_two, relation):
        for person in person_list:
            if person_name_one == person.name:
                for person_2 in person_list:
                    if person_name_two == person_2.name:
                        if person_2 in person.family_tree[relation]:
                            print("Yes")
                            return
                        else:
                            print("No")
                            return
        print("No")

    def closest_relation(self, person_two, person_one):
        if person_two in person_one.family_tree["spouse"]:
            print("spouse")
            return
        if person_two in person_one.family_tree["parent"]:
            print("parent")
            return
        if person_two in person_one.family_tree["sibling"]:
            print("sibling")
            return
        if person_two in person_one.family_tree["half-sibling"]:
            print("half-sibling")
            return
        if person_two in person_one.family_tree["ancestor"]:
            print("ancestor")
            return
        if person_two in person_one.family_tree["cousin"]:
            print("cousin")
            return
        else:
            print("Unrelated")
            return

def retrieve_person(person_name):
    for person in person_list:
        if person.name == person_name:
            return person

    x = Person(person_name)
    person_list.append(x)
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


def main():
    fileRead()

main()