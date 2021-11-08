import sys
class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge(self,p,mid,r):
        left_len = mid-p+1
        right_len = r-mid
        left_index,right_index = 0,0
        left_array = [0]*(left_len+1)
        right_array = [0]*(right_len+1)
        for i in range(0,left_len):
         left_array[i] = self.sorting_array[p+i]
        for i in range(0,right_len):
         right_array[i] = self.sorting_array[mid+1+i]
        left_array[left_len],right_array[right_len] = sys.maxsize,sys.maxsize
        for i in range(p,r+1):
         if left_array[left_index] <= right_array[right_index]:
                self.comparison_count = self.comparison_count + 1
                self.sorting_array[i] = left_array[left_index]
                left_index = left_index+1
         else:
                self.comparison_count = self.comparison_count + 1
                self.sorting_array[i] = right_array[right_index]
                right_index = right_index+1

    def merge_sort(self, p, r):
        if p < r:
            q = (p+r)//2
            self.merge_sort(p,q)
            self.merge_sort(q+1,r)
            self.merge(p,q,r)
        pass

    def max_heapify(self,A,i,n):
        left= 2*i + 1
        right= 2*i + 2
        if left<n and A[left]>A[i]:
            largest = left
            self.comparison_count = self.comparison_count + 1
        else:
            largest = i
            if left<n:
             self.comparison_count = self.comparison_count + 1
        if right<n and A[right]>A[largest]:
            largest = right
            self.comparison_count = self.comparison_count + 1
        else:
            if right<n:
              self.comparison_count = self.comparison_count + 1
        if largest != i:
            k=A[i]
            A[i]=A[largest]
            A[largest]=k
            self.max_heapify(A,largest,n)
    def build_max_heap(self,A,n):
        i = (n//2) -1
        while i>-1:
            self.max_heapify(A,i,n)
            i = i- 1
    def heap_sort(self):
        n = len(self.sorting_array)
        self.build_max_heap(self.sorting_array,n)
        i= n-1
        while i > 0:
            k=self.sorting_array[i]
            self.sorting_array[i]=self.sorting_array[0]
            self.sorting_array[0]=k
            self.max_heapify(self.sorting_array,0,i)
            i = i - 1
        pass

    def insertion_sort(self):
        i = 0
        for i in range(1,len(self.sorting_array)):
            x = self.sorting_array[i]
            j = i-1
            while x < self.sorting_array[j] and j>=0:
                self.comparison_count = self.comparison_count + 1
                self.sorting_array[j+1] = self.sorting_array[j]
                j = j-1
            self.sorting_array[j+1] = x
            if j>=0:
             self.comparison_count = self.comparison_count + 1
        pass
