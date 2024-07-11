class Patient:
    def __init__(self, priority, description):
        self.priority = priority  # Priority of the patient emergency
        self.patient = patient

class Emergency_Department:
    def __init__(self):
        self.heap = []
        self.resources_allocated_to=None
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].priority < self.heap[parent_index].priority:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index
            
            if left_child_index < len(self.heap) and self.heap[left_child_index].priority < self.heap[smallest].priority:
                smallest = left_child_index
            
            if right_child_index < len(self.heap) and self.heap[right_child_index].priority < self.heap[smallest].priority:
                smallest = right_child_index
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
    
    def add_patient(self, patient):
        self.heap.append(patient)
        self._heapify_up(len(self.heap) - 1)
        self.resource_allocated_to=self.heap[0]
    
    # Function to handle the highest priority emergency patient
    def handle_emergency_patient(self):
        if not self.heap:
            return None  
        
        p = self.heap[0]  
        self.heap[0] = self.heap[-1]  
        self.heap.pop()
        self.resource_allocated_to=None
        self._heapify_down(0)
        
        return p

    def check_emergency_patient(self):
        if not self.heap:
            return None  
        
        p = self.heap[0]
        self.resources_allocated_to=p
        return p
    def check_resource_allocation(self):
        print("Patient Name:",self.resources_allocated_to.patient)
        print("Emergency level:",self.resources_allocated_to.priority)

# Example usage:
management_system = Emergency_Department()

# Add patients to the system
management_system.add_patient(Patient(3, "John"))
management_system.add_patient(Patient(2, "Flora"))
management_system.add_patient(Patient(1, "Ben"))

# Handle patients based on priority
while True:
     p=management_system.handle_emergency_patient()
    if emergency:
        print(f"Handling emergency: {p.patient} (Priority: {p.priority})")
    else:
        print("No more patients in the system")
        break
