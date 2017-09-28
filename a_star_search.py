try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while not (q.empty()):
    print(q.get())

###############################
class State(object):

    def __init__(self,value,parent,start=0,goal=0):
        self.children=[]
        self.parent=parent
        self.value=value
        self.dist=0

        if parent:
            self.path=parent.path[:]
            self.path.append(value)
            self.start=parent.start
            self.goal=parent.goal
        else:
            self.path=[value]
            self.start=start
            self.goal=goal

    def get_dist(self):
            pass

    def create_children(self):
            pass

class State_string(State):

    def __init__(self,value,parent,start=0,goal=0):
        super(State_string,self).__init__(value,parent,start,goal)
        self.dist=self.get_dist()

    def get_dist(self):

        if (self.value==self.goal):
            return 0
        dist=0
        letter=""
        for i in range(len(self.goal)):
            letter=self.goal[i]
            dist+=abs(i-self.value.index(letter))
        return dist

    def create_children(self):
        print("entered create_children function.............")
        if not (self.children):
            val=""
            for i in range(len(self.goal)-1):
                val=self.value
                val=val[:i]+val[i+1]+val[i]+val[i+2:]
                print(i,val) ###############
                child=State_string(val,self) # self is for setting child's parent
                self.children.append(child)

class Astar_solver(object):
    def __init__(self, start, goal):
        self.path=[]
        self.visited_queue=[]
        self.priority_queue=Q.PriorityQueue()
        self.start=start
        self.goal=goal

    def solve(self):

        start_state=State_string(self.start,0,
                    self.start,self.goal)

        count=0
        self.priority_queue.put((0,count,start_state))
        ##################
        while ((not self.path) and self.priority_queue.qsize()):
            closest_child=self.priority_queue.get()[2]
            self.visited_queue.append(closest_child.value)
            closest_child.create_children()

            for child in closest_child.children:
                 if child.value not in self.visited_queue:
                    count+=1
                    if (child.dist==0):
                        self.path=child.path
                        break
                    print("Child.dist :",child.dist)
                    print("Count :",count)
                    self.priority_queue.put((child.dist,count,child))
        if not self.path:
                    print("Goal ",self.goal," is not possible")
                
##################

##==========================
#MAIN

if __name__=="__main__":
        start1="cdabfe"
        goal1="abcdef"
        a=Astar_solver(start1,goal1)
        a.solve()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ANSWER")
        for i in range(len(a.path)):
                print(i," ) ",a.path[i])
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! upto here")
        print(a.visited_queue)

