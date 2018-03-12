class mystack(object):

    item = list()

    def add_item(self, *L):
        for it in L:
            item.append(it)

    def pop_item(self):
        return item.pop()

    def count_items(self):
        return len(item)


