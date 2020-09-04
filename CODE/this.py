class SearchingSorting:

    def swap(self, A, x, y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp

    def linear_search(self, item, my_list):
        self.found = False
        self.position = 0
        while self.position < len(my_list) and not self.found:
            if my_list[self.position] == item:
                self.found = True
            self.position = self.position + 1
        print('found??' + str(self.found))
        return self.found

    def selection_sort(self, alist):
        for i in range(len(alist)):
            self.least = i
            for k in range(i + 1, len(alist)):
                if int(alist[k]) < int(alist[self.least]):
                    self.least = k

            SearchingSorting.swap(self, alist, self.least, i)
            
            
            
