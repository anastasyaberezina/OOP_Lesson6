def add_spouse(self, spouse):
        if spouse not in self.family['spouse']:
            self.family['spouse'].append(spouse)
        if self not in spouse.family['spouse']:
            spouse.family['spouse'].append(self)

def add_siblings(self, parent_one, parent_two):
    for child in parent_one.family['children']:
        if child not in self.family['sibling'] and self.name is not child.name:
            if child in parent_two.family_tree['children']:
                self.family['sibling'].append(child)
                child.add_siblings(parent_one, parent_two)
            else:
                self.family['half-sibling'].append(child)
                if self not in child.family['half-sibling']:
                    child.family['half-sibling'].append(self)

        if self not in child.family['cousin']:
            child.family['cousin'].append(self)
        if child not in self.family['cousin']:
            self.family['cousin'].append(child)

    for child in parent_two.family['children']:
        if child not in self.family['sibling'] and self.name is not child.name:
            if child in parent_one.family['children']:
                self.family['sibling'].append(child)
                child.add_siblings(parent_one, parent_two)
            else:
                self.family['half-sibling'].append(child)
                if self not in child.family['half-sibling']:
                    child.family['half-sibling'].append(self)

        if self not in child.family['cousin']:
            child.family['cousin'].append(self)
        if child not in self.family['cousin']:
            self.family['cousin'].append(child)

def add_cousins(self, parent_one, parent_two):
    for p in person_list:
        for ancestor in self.family['ancestor']:
            if ancestor in p.family['ancestor'] and p not in self.family['cousin']:
                self.family['cousin'].append(p)
                if self not in p.family['cousin']:
                    p.family['cousin'].append(self)

    for cousin in parent_one.family['cousin']:
        if cousin not in self.family['cousin']:
            self.family['cousin'].append(cousin)
        if self not in cousin.family['cousin']:
            cousin.family['cousin'].append(self)

    for cousin in parent_two.family['cousin']:
        if cousin not in self.family['cousin']:
            self.family['cousin'].append(cousin)
        if self not in cousin.family['cousin']:
            cousin.family['cousin'].append(self)

    for sibling in parent_one.family['sibling']:
        if sibling not in self.family['cousin']:
            self.family['cousin'].append(sibling)
        if self not in sibling.family['cousin']:
            sibling.family['cousin'].append(self)

    for halfsib in parent_one.family['half-sibling']:
        if halfsib not in self.family['cousin']:
            self.family['cousin'].append(halfsib)
        if self not in halfsib.family['cousin']:
            halfsib.family['cousin'].append(self)

    for sibling in parent_two.family['sibling']:
        if sibling not in self.family['cousin']:
            self.family['cousin'].append(sibling)
        if self not in sibling.family['cousin']:
            sibling.family['cousin'].append(self)

    for halfsib in parent_two.family['half-sibling']:
        if halfsib not in self.family['cousin']:
            self.family['cousin'].append(halfsib)
        if self not in halfsib.family['cousin']:
            halfsib.family['cousin'].append(self)
