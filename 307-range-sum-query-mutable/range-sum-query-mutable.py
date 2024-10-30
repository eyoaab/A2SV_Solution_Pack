
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0 for i in range(len(nums) * 4)]
        self.arr = nums
        self.build(0,0,len(nums) - 1)
           

    def update(self, index: int, val: int) -> None:
        self.customUpdate(0,0,len(self.arr) - 1,index,val)
        

    def sumRange(self, left: int, right: int) -> int:

        return self.query(0,0, len(self.arr) - 1,left, right)




    
    def getchild(self,n):
        left = 2 * n + 1
        right = 2 * n + 2

        return left,right


    def build(self,node,nleft,nright):
        if nleft == nright:
            self.tree[node] = self.arr[nleft]
            return

        mid = (nleft + nright ) // 2


        leftChild,rightChild = self.getchild(node)   

        self.build(leftChild,nleft,mid)
        self.build(rightChild,mid + 1,nright)

        self.tree[node] = self.tree[leftChild] + self.tree[rightChild] 
    
    def customUpdate(self,node,leftBound,rightBound,index,value):
        if leftBound == rightBound:
            self.tree[node] = value
            self.arr[index] = value
            return

        mid = (leftBound + rightBound) // 2
        leftChild,rightChild = self.getchild(node)

        if index <= mid:
            self.customUpdate(leftChild,leftBound,mid,index,value)
        else:  
            self.customUpdate(rightChild,mid + 1,rightBound,index,value)

        self.tree[node] = self.tree[leftChild] +  self.tree[rightChild]    

    def query(self, node, nLeft, nRight, qLeft, qRight):
        if qLeft > qRight:
            return 0
        # print(node)
        if qLeft == nLeft and qRight == nRight:
            return self.tree[node]

        mid = nLeft + (nRight - nLeft) // 2
        left_child, right_child = self.getchild(node)
       
        left_sum = self.query(left_child, nLeft, mid, qLeft, min(qRight, mid))
        right_sum = self.query(right_child, mid + 1, nRight, max(qLeft, mid + 1), qRight)
        
        return left_sum + right_sum 
    

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)